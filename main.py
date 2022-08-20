__author__ = 'Jeremy Atia'

import sys
import pandas as pd
import streamlit as st
from users import Users
from leaderboard import LeaderBoard
from templates import overview, data, evaluation
from streamlit.cli import main as stmain
from config import Y_TEST_GOOGLE_PUBLIC_LINK, SKLEARN_SCORER, GREATER_IS_BETTER, SKLEARN_ADDITIONAL_PARAMETERS

@st.cache
def load_target(google_link: str) -> pd.DataFrame:
    url='https://drive.google.com/uc?id=' + google_link.split('/')[-2]
    y_test = pd.read_csv(url, index_col=0)
    return y_test


def evaluate(y_true, y_pred, callable, additional_parameters=SKLEARN_ADDITIONAL_PARAMETERS):
    return callable(y_true, y_pred, **additional_parameters)


def main():
    st.header('Datathon Platform')
    ldb = LeaderBoard()
    users = Users()

    # Sidebar Navigation
    st.sidebar.title('Navigation')
    options = st.sidebar.radio('Select a page:',
                               ['Overview', 'Data', 'Evaluation', 'Submit'])

    if options in ['Overview', 'Data', 'Evaluation']:
        st.markdown(eval(options.lower()), unsafe_allow_html=True)

    else:
        with st.sidebar:
            login = st.text_input('login')
            password = st.text_input('password')

        if users.exists(login, password):
            st.write('Welcome', login)
            st.markdown('Submit the test predictions as a csv file ordered the same way as given, in the example.')
            
            if users.is_admin(login, password):
                with st.sidebar:
                    st.write("***************")
                    st.write("Manage the app")
                    pause_datathon = st.checkbox("Pause Datathon", value=not(is_datathon_running()))
                    change_datathon_status(pause_datathon)

            uploaded_file = st.file_uploader('Predictions', type='csv', accept_multiple_files=False)
            leaderboard = ldb.get()
            if uploaded_file is not None and is_datathon_running():
                y_pred = pd.read_csv(uploaded_file, index_col=0)
                y_test = load_target(google_link=Y_TEST_GOOGLE_PUBLIC_LINK)
                score = evaluate(y_test, y_pred, callable=SKLEARN_SCORER)
                st.write("Your score is", score)
                leaderboard = ldb.edit(leaderboard, id=login, score=score)

            with st.expander("Show leaderboard", expanded=True):
                st.write(ldb.show(leaderboard, ascending=not(GREATER_IS_BETTER)))
        else:
            st.info("Please enter a valid login/password on the left side bar.")

def is_datathon_running() -> bool:
    with open('STATUS_DATATHON.txt', 'r') as f:
        content = f.readline()
    if content == 'running':
        return True
    else:
        return False

def change_datathon_status(pause_datathon: bool) -> None:
    if pause_datathon:
        with open('STATUS_DATATHON.txt', 'w') as f:
            f.write('pause')
    else:
        with open('STATUS_DATATHON.txt', 'w') as f:
            f.write('running')


if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stmain())

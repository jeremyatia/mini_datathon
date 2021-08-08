import pandas as pd
import streamlit as st
from users import Users
from leaderboard import LeaderBoard
from sklearn.metrics import average_precision_score
from templates import overview, data, evaluation
train_test_sampling = {'frac': 0.7, 'random_state': 35}


@st.cache
def load_target():
    labels = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/secom/secom_labels.data',
                         header=None, sep=' ', names=['target', 'time'])
    y_train = labels.sample(**train_test_sampling)
    y_test = labels.loc[~labels.index.isin(y_train.index), 'target']
    return y_test


def evaluate(y_true, y_pred):
    return average_precision_score(y_true, y_pred, average='micro')


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
            st.markdown('Submit the test predictions as a csv file ordered the same way as given, with the column `predictions`')
            uploaded_file = st.file_uploader('Predictions', type='csv', accept_multiple_files=False)

            if uploaded_file is not None:
                y_pred = pd.read_csv(uploaded_file)['predictions']
                y_test = load_target()
                score = evaluate(y_test, y_pred)
                st.write("Your score is", score)
                leaderboard = ldb.get()
                new_lb = ldb.edit(leaderboard, id=login, score=score)
                with st.beta_expander("Show leaderboard"):
                    st.write(ldb.show(new_lb, ascending=False))
        else:
            st.info("Please enter a valid login/password")


if __name__ == "__main__":
    main()

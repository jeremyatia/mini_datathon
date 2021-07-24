import pandas as pd
import streamlit as st
from users import Users
from leaderboard import LeaderBoard
from sklearn.metrics import average_precision_score


def load_target():
    return pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/secom/secom_labels.data', header=None,
                       sep=' ', names=['target', 'time']).iloc[:, 0]


def evaluate(y_true, y_pred):
    return average_precision_score(y_true, y_pred, average='micro')


def main():
    st.header('Datathon Platform')
    ldb = LeaderBoard()
    users = Users()

    with st.sidebar:
        login = st.text_input('login')
        password = st.text_input('password')

    if users.exists(login, password):
        st.write('Welcome', login)
        y_true = load_target()
        uploaded_file = st.file_uploader('Predictions', type='csv', accept_multiple_files=False)

        if uploaded_file is not None:
            y_pred = pd.read_csv(uploaded_file)['predictions']
            score = evaluate(y_true, y_pred)
            st.write("Your score is", score)
            leaderboard = ldb.get()
            new_lb = ldb.edit(leaderboard, id=login, score=score)
            with st.beta_expander("Show leaderboard"):
                st.write(ldb.show(new_lb, ascending=False))
    else:
        st.info("Please enter a valid login/password")


if __name__ == "__main__":
    main()

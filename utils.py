import base64

# @st.cache
# def load_data():
#     df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/secom/secom.data',
#                      sep=' ', header=None)
#     labels = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/secom/secom_labels.data',
#                          header=None, sep=' ', names=['target', 'time']).iloc[:, 0]
#     X_train = df.sample(**train_test_sampling)
#     y_train = labels.loc[X_train.index]
#     X_test = df.loc[~df.index.isin(X_train.index), :]
#     y_test = labels.loc[X_test.index]
#     return X_train, y_train, X_test, y_test

# st.markdown(data, unsafe_allow_html=True)
# if st.button('Load data'):
#     X_train, y_train, X_test, y_test = load_data()
#     st.markdown(get_table_download_link(X_train, filename='X_train.csv'), unsafe_allow_html=True)
#     st.markdown(get_table_download_link(y_train, filename='y_train.csv'), unsafe_allow_html=True)
#     st.markdown(get_table_download_link(X_test, filename='X_test.csv'), unsafe_allow_html=True)


def get_table_download_link(df, filename):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download {filename}</a>'

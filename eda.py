import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#webapp ka title
st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by codanics youtube channel called **EDA app**
''')
#how to upload a file from pc

with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=["csv"]) 
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV File](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download)")

# profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative= True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file')
    if st.button('Press to use example data'):
        # example data set

        def load_data():
            a = pd.DataFrame( np.random.rand(100, 5),
                             columns=['apple', 'ball','cat', 'dog', 'Ear' ])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative= True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)
        


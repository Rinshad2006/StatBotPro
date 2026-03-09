import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("StatBotPro - AI Data Analyst")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write("Dataset Preview")
    st.write(df.head())

    question = st.text_input("Ask a question about your data")

    if question:

        if "chart" in question.lower() or "graph" in question.lower():

            numeric_columns = df.select_dtypes(include="number").columns

            if len(numeric_columns) > 0:

                column = numeric_columns[0]

                plt.figure()
                df[column].plot(kind="bar")

                st.pyplot(plt)

        else:

            st.write("Question received:", question)
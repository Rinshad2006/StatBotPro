import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 StatBotPro - Autonomous CSV Data Analyst")

st.write("Upload a CSV file and analyze your dataset.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset info
    st.subheader("Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.write("Column Names:")
    st.write(df.columns.tolist())

    # Statistics
    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        st.subheader("Basic Statistics")
        st.write(df.describe())

    # Chart section
    st.subheader("Data Visualization")

    if len(numeric_columns) > 0:

        selected_column = st.selectbox(
            "Select numeric column for chart",
            numeric_columns
        )

        fig, ax = plt.subplots()
        df[selected_column].plot(kind="bar", ax=ax)

        st.pyplot(fig)

    # Ask questions section
    st.subheader("Ask Questions About Your Data")

    question = st.text_input("Ask a question about your dataset")

    if question:

        q = question.lower()

        if "rows" in q or "how many rows" in q:
            st.write(f"Total rows: {len(df)}")

        elif "columns" in q:
            st.write(f"Total columns: {len(df.columns)}")

        elif "highest" in q or "max" in q:
            col = numeric_columns[0]
            st.write(f"Highest value in {col}: {df[col].max()}")

        elif "average" in q or "mean" in q:
            col = numeric_columns[0]
            st.write(f"Average value in {col}: {df[col].mean()}")

        elif "sum" in q or "total" in q:
            col = numeric_columns[0]
            st.write(f"Total of {col}: {df[col].sum()}")

        else:
            st.write("⚠️ Sorry, I couldn't understand that question yet.")
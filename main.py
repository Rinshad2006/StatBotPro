from sandbox_runner import run_code_safely
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOllama


print("Program started...")

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API Key Loaded")

df = pd.read_csv("data.csv")

print("CSV Loaded")

llm = ChatOllama(
    model="llama3"
)

print("LLM Ready")

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    allow_dangerous_code=True,
    agent_executor_kwargs={"handle_parsing_errors": True}
)

print("Agent Ready")


def create_revenue_chart(df):

    # Create charts folder if it doesn't exist
    os.makedirs("charts", exist_ok=True)

    revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))

    bars = plt.bar(revenue.index, revenue.values)

    plt.title("Total Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Add numbers on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom"
        )

    filepath = "charts/revenue_by_region.png"

    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()

    return filepath


while True:

    question = input("\nAsk a question about the CSV: ")

    if question.lower() == "exit":
        break

    if "chart" in question.lower() or "graph" in question.lower():
        path = create_revenue_chart(df)
        print(f"Chart saved at: {path}")

    else:
        response = agent.invoke({"input": question})

        print("\nAnswer:")
        print(response["output"])
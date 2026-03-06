import pandas as pd
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
    verbose=True,
    allow_dangerous_code=True
)

print("Agent Ready")

while True:

    question = input("\nAsk a question about the CSV: ")

    if question.lower() == "exit":
        break

    response = agent.run( question)
    print(response)

    print("\nAnswer:")
    print(response["output"])
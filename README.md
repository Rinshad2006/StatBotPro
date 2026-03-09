 StatBotPro 

StatBotPro is an AI-powered CSV data assistant built with Python.
It allows users to ask natural language questions about a dataset, and the AI agent analyzes the CSV file to generate answers.

  Features

* Ask questions about CSV datasets using natural language
* Automatically loads and analyzes data using Python
* Uses OpenAI LLM to understand queries
* Built with LangChain agent framework
* Easy to run locally

Example questions:

* "How many rows are in the dataset?"
* "Show first 5 rows"
* "What is the average value of column X?"
* "Which category appears most?"

---

  Tech Stack

* Python
* Pandas
* LangChain
* OpenAI API
* Python-dotenv

---

 Project Structure

StatBotPro
│
├── main.py          # Main program
├── data.csv         # Dataset file
├── .env             # API key file
├── requirements.txt # Dependencies
└── README.md        # Project documentation

---

  Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/StatBotPro.git
cd StatBotPro
```

2️⃣ Create virtual environment

```bash
python -m venv venv
```

3️⃣ Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

 Setup API Key

Create a `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

---

 Run the Project

```bash
python main.py
```

Then ask questions about your dataset.

Example:

```
Ask a question about the CSV: show first 5 rows
```

---

 Example Output

```
Program started...
API Key Loaded
CSV Loaded
LLM Ready
Agent Ready

Ask a question about the CSV:

Week 2 – Data Visualization 📊

In Week 2, the StatBotPro project was enhanced with data visualization capabilities.

Features added:

- The AI agent can now generate charts from the CSV dataset.
- Uses **Matplotlib** for plotting graphs.
- The agent automatically runs Python code to analyze and visualize data.
- Charts can be generated using natural language queries.

Example prompts:

- "Show first 5 rows"
- "Plot the distribution of sales"
- "Create a bar chart of the Region column"

Example output:

The agent generates charts using Python and saves them as images.
```

---

Week 3 – Sandbox Execution

In Week 3, a secure sandbox environment was implemented.

Features:
- AI generated code is checked before execution
- Dangerous commands are blocked
- Code runs in a restricted environment
- Improves security and reliability of the system

----

Week 4 – Web Interface

In Week 4, a web interface was built using Streamlit.

Features:
- Upload CSV file
- Ask questions about dataset
- Generate charts
- Interactive web interface
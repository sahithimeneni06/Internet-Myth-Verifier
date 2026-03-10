# 🔎 Internet Myth Verification Agent

An AI-powered system that verifies common internet claims using multiple sources and LLM reasoning.

Many claims on the internet spread quickly without proper verification. This project builds an **AI agent that searches the web, analyzes evidence, and provides a verified conclusion** for user-submitted claims.

---

## 🚀 Project Overview

The **Internet Myth Verification Agent** helps users determine whether a statement circulating online is **true, false, or misleading**.

Example claims:

* *Drinking cold water causes heart attack*
* *Eating carrots drastically improves eyesight*
* *AI will replace all jobs*

The agent retrieves information from the web and uses an LLM to analyze and summarize the evidence.

---

## 🧠 How the System Works

The system follows an **agentic reasoning workflow**:

User Claim
↓
AI Agent
↓
Web Search Tool
↓
Collect Evidence
↓
Analyze Sources
↓
Generate Verdict

The agent uses the **ReAct reasoning pattern**:

Thought → Action → Observation → Final Answer

---

## ⚙️ Technologies Used

* **Python**
* **LangChain**
* **Groq LLM API**
* **DuckDuckGo Search Tool**
* **Streamlit (for UI)**

---

## 🔧 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/Internet_Myth_Checker.git
cd Internet_Myth_Checker
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Set up environment variables

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Project

### Run CLI version

```
python main.py
```


### Run Streamlit App

```
streamlit run app_streamlit.py
```

Then open the browser at:

```
http://localhost:8501
```

---

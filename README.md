# LangChain LLM Chain – Basic Tutorial Implementation
- Jeimy Alejandra Yaya Martinez

## 📌 Overview

This repository contains the implementation of the basic **LangChain LLM Chain tutorial** using OpenAI models.

The objective of this project is to understand how LangChain structures interactions with Large Language Models (LLMs) by combining:

- Prompt templates  
- Language models  
- Output parsers  
- Chain composition  

This project represents the foundational step before building more advanced systems such as Retrieval-Augmented Generation (RAG).

---

## 🏗️ Architecture

The application follows a simple sequential pipeline:

User Input  
→ Prompt Template  
→ Gemini LLM    
→ Output Parser  
→ Final Response  

### Components Explained

- **ChatPromptTemplate**  
  Defines the structure of system and user messages.

- **ChatGoogleGenerativeAI**  
  Connects to Google's Gemini model (`gemini-2.5-flash`).

- **StrOutputParser**  
  Converts the model's structured output into a readable string.

- **LCEL (LangChain Expression Language)**  
  The `|` operator composes components into a runnable chain.

---

## 🛠️ Technologies Used

- Python 3.10+
- LangChain
- Google Gemini API
- langchain-google-genai
- python-dotenv

---

## 📂 Project Structure
```
langchain-llm-chain-intro/
│
├── main.py
├── requirements.txt
├── .env (not included in repo)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/langchain-llm-chain-intro.git
cd langchain-llm-chain-intro
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
---

### 🔐 Environment Variables
Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```
---

### ▶️ Running the Project

Run:

```bash
python main.py
```

The program will ask you to enter a topic.


Example:
```bash
Enter a topic: Retrieval-Augmented Generation
```
Example output:
<img width="1618" height="834" alt="image" src="https://github.com/user-attachments/assets/e33b29f9-f6f7-4037-90d5-24a17f25f44e" />

--- 
### 🚀 Key Learnings

LLM Chains allow modular composition of AI workflows.

- Prompt templates separate logic from user input.
- Output parsers standardize model responses.
- This architecture serves as the foundation for more advanced systems like RAG.

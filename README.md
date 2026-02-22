# LangChain LLM Chain – Basic Tutorial Implementation

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
→ OpenAI LLM  
→ Output Parser  
→ Final Response  

### Components Explained

- **ChatPromptTemplate**  
  Defines the structure of system and user messages.

- **ChatOpenAI**  
  Connects to OpenAI’s chat model (`gpt-4o-mini`).

- **StrOutputParser**  
  Converts the model's structured output into a readable string.

- **LCEL (LangChain Expression Language)**  
  The `|` operator composes components into a runnable chain.

---

## 🛠️ Technologies Used

- Python 3.10+
- LangChain
- OpenAI API
- python-dotenv

---

## 📂 Project Structure

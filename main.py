import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Explain the concept of {topic} in simple terms.")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Dynamic input
topic = input("Enter a topic: ")

response = chain.invoke({"topic": topic})

print("\nResponse:\n")
print(response)
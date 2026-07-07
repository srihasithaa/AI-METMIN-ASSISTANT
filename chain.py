from langchain_ollama import ChatOllama
from prompts import template

llm=ChatOllama(
    model="gemma3:4b"
)

chain = template | llm
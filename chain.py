from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama
from prompts import template
from memory import chat_history

llm=ChatOllama(
    model="gemma3:4b"
)

chain = template | llm

conversation_chain = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history,
    history_messages_key="history",
    input_messages_key="question"
)
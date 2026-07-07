from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from loaders import meeting_minutes

template=ChatPromptTemplate(
    [
        ("system", "You are an AI assistant that answers questions about meeting minutes."
                   "Use only the provided meeting content.Do not invent or assume details."
                   "If the answer isn't present, say you don't know based on the meeting minutes."
                   "Meeting Minutes: {meeting_minutes}"),
        MessagesPlaceholder("history"),
        ("human", "{question}")
    ]
)

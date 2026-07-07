from langchain_core.prompts import ChatPromptTemplate
from loaders import meeting_minutes

template=ChatPromptTemplate(
    [
        ("system", "You are an AI assistant that answers questions about meeting minutes."
                   "Use only the provided meeting content.Do not invent or assume details."
                   "If the answer isn't present, say you don't know based on the meeting minutes."
                   "Meeting Minutes: {meeting_minutes}"),
        ("human", "{question}")
    ]
)
def prompt_template(question):
    result=template.invoke(
        {
            "meeting_minutes": meeting_minutes(),
            "question": question
        }
    )
    return result
from loaders import meeting_minutes
from chain import chain

user_question=input("Question: ")
meeting_content=meeting_minutes()

response=chain.invoke(
    {
        "meeting_minutes": meeting_content,
        "question": user_question
    }
)
print(response.content)

from loaders import meeting_minutes
from chain import conversation_chain

meeting_content=meeting_minutes()
while True:
    user_question=input("Question: ")

    if user_question.upper()=="EXIT":
        break

    response=conversation_chain.invoke(
        {
            "meeting_minutes": meeting_content,
            "question": user_question

        },
        config={
            "configurable": {
                "session_id": "1"
            }
        }
    )
    print(response.content)

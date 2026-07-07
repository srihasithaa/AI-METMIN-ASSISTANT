from langchain_community.document_loaders import TextLoader

def meeting_minutes():
    loader=TextLoader("documents/meeting.txt")
    doc=loader.load()
    meeting_content=doc[0].page_content
    return meeting_content

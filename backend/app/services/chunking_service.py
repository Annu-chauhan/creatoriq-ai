from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    return splitter.split_text(text)
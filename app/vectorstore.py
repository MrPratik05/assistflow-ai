from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from app.config import CHUNK_SIZE, CHUNK_OVERLAP, VECTOR_DB_PATH
from app.loader import load_support_documents
from app.embeddings import get_embeddings


def build_vectorstore():
    documents = load_support_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=str(VECTOR_DB_PATH),
    )

    return vectorstore


def load_vectorstore():
    vectorstore = Chroma(
        persist_directory=str(VECTOR_DB_PATH),
        embedding_function=get_embeddings(),
    )

    return vectorstore
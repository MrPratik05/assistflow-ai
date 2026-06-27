from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


DATA_PATH = Path("data/support_docs.txt")
CHROMA_PATH = "chroma_db"


def load_support_docs():
    text = DATA_PATH.read_text(encoding="utf-8")
    return [Document(page_content=text)]


def create_vectorstore():
    documents = load_support_docs()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    return vectorstore


def get_retriever():
    vectorstore = create_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 3})
from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
)

KNOWLEDGE_BASE = Path("knowledge_base")


def load_support_documents():
    """
    Load all supported documents from the knowledge_base folder.
    Supports:
        - TXT
        - PDF
        - DOCX
    """

    documents = []

    # Load TXT files
    txt_folder = KNOWLEDGE_BASE / "txt"

    for file in txt_folder.glob("*.txt"):
        loader = TextLoader(str(file), encoding="utf-8")
        documents.extend(loader.load())

    # Load PDF files
    pdf_folder = KNOWLEDGE_BASE / "pdf"

    for file in pdf_folder.glob("*.pdf"):
        loader = PyPDFLoader(str(file))
        documents.extend(loader.load())

    # Load DOCX files
    docx_folder = KNOWLEDGE_BASE / "docx"

    for file in docx_folder.glob("*.docx"):
        loader = Docx2txtLoader(str(file))
        documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents.")

    return documents
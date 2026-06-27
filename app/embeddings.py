from langchain_huggingface import HuggingFaceEmbeddings

from app.config import EMBEDDING_MODEL


def get_embeddings():
    """
    Returns the embedding model used for vector search.
    """

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
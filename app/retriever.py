from app.config import TOP_K_RESULTS
from app.vectorstore import load_vectorstore


def get_retriever():
    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K_RESULTS}
    )

    return retriever
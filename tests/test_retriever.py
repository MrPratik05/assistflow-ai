from app.retriever import get_retriever

retriever = get_retriever()

question = "What is the refund policy?"

docs = retriever.invoke(question)

print("Retrieved documents:")
print("--------------------")

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}:")
    print(doc.page_content)
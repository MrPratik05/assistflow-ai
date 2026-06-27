from app.loader import load_support_documents

documents = load_support_documents()

print("Number of documents:", len(documents))
print()
print("Document content:")
print(documents[0].page_content[:500])  # Print the first 500 characters
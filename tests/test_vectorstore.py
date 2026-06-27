from app.vectorstore import create_vectorstore

vectorstore = create_vectorstore()

print("Vector store created successfully!")
print("Collection name:", vectorstore._collection.name)
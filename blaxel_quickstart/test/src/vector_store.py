import chromadb

client = chromadb.PersistentClient(path="data/chroma")
collection = client.get_or_create_collection(
    "memory",
    metadata={"hnsw:space": "cosine"} #cosine similarity (focuses on the direction of vector emeddings.)
)

def add_embedding(id, text, embedding):
    collection.add(ids=[id], documents=[text], embeddings=[embedding])

def search_embeddings(embedding, k=5):
    return collection.query(query_embeddings=[embedding], n_results=k)

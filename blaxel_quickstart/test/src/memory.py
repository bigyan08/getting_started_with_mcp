import uuid
from embeddings import embed
from vector_store import add_embedding, search_embeddings,collection
from llm import call_llm

def list_notes():
    data = collection.get()
    if not data or "documents" not in data:
        return []
    docs = data["documents"]
    ids = data["ids"]
    output = []
    for i,d in enumerate(docs):
        output.append({
            "id":ids[i],
            "text":d
        })
    return output

def add_note(text: str):
    emb = embed(text=text)
    note_id = str(uuid.uuid4())
    add_embedding(note_id,text,emb)
    return {"id":note_id,"message":"Note saved."}


def search_memory(query: str):
    emb = embed(text=query) #embed the query
    results = search_embeddings(emb) # find the top k results
    docs = results['documents'][0] #since chromadb saves in batches so we use the first batch of docs.
    ids = results['ids'][0] # its ids
    context = "\n".join(docs)
    ans = call_llm(f"Use this context:{context} \n Answer the query:{query}")
    return {"matches":list(zip(docs,ids)),"answer":ans}

def summarize_recent():
    q_emb = embed(text="recent notes")
    results = search_embeddings(q_emb,k=10)
    docs = results['documents'][0]
    combined_docs = "\n".join(docs)
    summarized_content = call_llm(f"Summarize these notes:{combined_docs}")
    return summarized_content

def summarize(text:str):
    summary = call_llm(f"Summarize this text:{text}")
    return summary
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/e5-large")

def embed(text: str):
    return model.encode(text, normalize_embeddings=True).tolist()

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=300):
    text = re.sub(r'\s+', ' ', text)
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def build_faiss_index(chunks):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return index, embeddings

def search(query, chunks, index, top_k=3):
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb).astype('float32'), top_k)
    return [chunks[i] for i in indices[0]]

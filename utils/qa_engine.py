# utils/qa_engine.py

import numpy as np
from utils.text_loader import TextLoader
from utils.embedder import Embedder
from faiss import IndexFlatL2

# Add threshold to ensure relevance
def retrieve_context(query, embeddings, index, id_mapping, threshold=0.30, top_k=3):
    """
    Retrieve context for a query from FAISS index.
    Args:
        query: The query text.
        embeddings: The embedding model to generate query vectors.
        index: The FAISS index.
        id_mapping: Mapping from indices to document IDs.
        threshold: Minimum similarity threshold for context relevance.
        top_k: Number of top results to retrieve.
    Returns:
        A tuple containing:
        - The top-k retrieved chunks of text
        - The best similarity score
    """
    query_emb = embeddings.embed_query(query)
    scores, indices = index.search(np.array([query_emb]), top_k)

    # Highest similarity score
    best_score = scores[0][0]

    # Check if similarity is too low
    if best_score < threshold:
        return None, best_score   # Return None if context is irrelevant

    chunks = [id_mapping[i] for i in indices[0] if i in id_mapping]
    return chunks, best_score

def generate_answer(query, embeddings, index, id_map):
    """
    Generate an answer for the given query based on document context.
    Args:
        query: The user query text.
        embeddings: The embedding model to generate query vectors.
        index: The FAISS index.
        id_map: A mapping from document IDs to actual content.
    Returns:
        The generated answer from the LLM or a default message if no context is found.
    """
    chunks, score = retrieve_context(query, embeddings, index, id_map)

    if chunks is None:
        return "No relevant answer found in the document."  # Return this if no context is found

    context = "\n\n".join(chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer briefly:"
    
    # Process the prompt using the LLM
    response = get_llm_response(prompt)  # Assuming there's a function for generating responses from LLM
    return response

import streamlit as st
from utils.text_loader import load_text
from utils.embedder import chunk_text, build_faiss_index, search
from utils.qa_engine import answer_question

st.set_page_config(page_title="DocuMind-LLM – AI-powered Q&A", page_icon="📄")
st.title("📄 DocuMind-LLM – AI-powered Q&A Chatbot")

uploaded_file = st.file_uploader("Upload a PDF or text file", type=["pdf", "txt"])

if uploaded_file:
    st.info("Processing document...")
    text = load_text(uploaded_file)
    chunks = chunk_text(text)
    index, _ = build_faiss_index(chunks)
    st.success("Document indexed successfully!")

    query = st.text_input("Ask a question about your document:")

    if query:
        top_contexts = search(query, chunks, index)
        context = " ".join(top_contexts)
        answer = answer_question(query, context)
        st.subheader("🧠 Answer:")
        st.write(answer)

# 🧠 DocuMind LLM — Intelligent Document Q&A Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow)
![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-brightgreen)
![LangChain](https://img.shields.io/badge/Framework-LangChain-lightblue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project%20Status-Active-success)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange)
![Stars](https://img.shields.io/github/stars/ramarav/DocuMind-LLM?style=social)
![Forks](https://img.shields.io/github/forks/ramarav/DocuMind-LLM?style=social)
![Last Commit](https://img.shields.io/github/last-commit/ramarav/DocuMind-LLM)

---

DocuMind LLM is a **Generative AI-powered document assistant** built with **Hugging Face Transformers**, **FAISS**, and **LangChain**.  
It allows users to upload PDF files, intelligently index their contents, and **ask natural language questions** about the document.

---

## 🚀 Features

- 📄 **PDF Upload & Parsing** — Extracts text and chunks it for semantic understanding.  
- 🤖 **LLM-powered Q&A** — Uses a Transformer model (e.g., `mistralai/Mixtral`, `google/flan-t5`, etc.) to answer questions.  
- ⚡ **FAISS-based Vector Search** — Enables fast and accurate document retrieval.  
- 💬 **Conversational Memory** — Keeps track of your recent queries for context-aware responses.  
- 🧩 **Modular Architecture** — Easy to extend with other models, vector stores, or APIs.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Embeddings | Hugging Face Sentence Transformers |
| Vector Store | FAISS |
| LLM | Hugging Face Transformers |
| Interface | Streamlit / Flask |
| Backend | Python 3.10+ |

---

## ⚙️ Installation

```bash
git clone https://github.com/ramarav/DocuMind-LLM.git
cd DocuMind-LLM
pip install -r requirements.txt
```

---

## 🧠 Usage

### 1️⃣ Start the App

```bash
python app.py
```

### 2️⃣ Upload a PDF file
Choose any `.pdf` document you want to query.

### 3️⃣ Ask Questions
Type natural language questions like:

> “What are the main topics covered in this document?”  
> “Summarize section 3.”  
> “What are the key takeaways?”

---

## 📚 Example Use Cases

- Research paper summarization  
- Legal contract question answering  
- Technical documentation assistant  
- Corporate report analysis  
- AI-based knowledge discovery

---

## 🧑‍💻 Folder Structure

```
DocuMind-LLM/
│
├── app.py                # Main entry point
├── utils/                # Helper scripts
│   ├── pdf_loader.py
│   ├── embedder.py
│   ├── vector_store.py
│   └── qa_engine.py
├── sample.pdf            # Example document
├── requirements.txt
└── README.md
```

---

## 🪄 Future Enhancements

- Add **chat history memory** using LangChain.  
- Integrate **OpenAI API** for comparison.  
- Enable **multi-file document search**.  
- Add **semantic summarization** features.

---

## 🏆 Credits

Developed by **Mekala Ramarao**  
💼 AMD India | AI/ML Engineer  
🔗 [LinkedIn](https://www.linkedin.com/in/mekala-ramarao-a2b5a562/) • [GitHub](https://github.com/ramarav)
---

## 📜 License

This project is licensed under the **MIT License**.

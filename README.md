# Website-Based Chatbot using Embeddings

## 📌 Overview
This project is an AI-powered website-based chatbot that answers user questions **strictly using the content of a provided website URL**.  
It uses web scraping, text chunking, embeddings, vector search, and an LLM to build a Retrieval-Augmented Generation (RAG) system.

The chatbot **does not hallucinate** and returns a fixed response when the answer is not present on the website.

---

## 🧠 Architecture

Website URL
↓
Web Scraper (BeautifulSoup)
↓
Text Cleaning & Chunking
↓
Embedding Generation
↓
Vector Database (FAISS)
↓
Similarity Search
↓
LLM (FLAN-T5)
↓
Answer (Website-grounded)


---

## ⚙️ Technologies Used

| Component | Tool |
|--------|------|
| Language | Python |
| UI | Streamlit |
| Web Scraping | BeautifulSoup, Requests |
| Text Chunking | Custom logic |
| Embeddings | Sentence-Transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS |
| LLM | google/flan-t5-base |
| Framework | Custom RAG (no RetrievalQA dependency) |

---

## 🧬 Embedding Strategy

- Website text is split into overlapping chunks
- Each chunk is converted into a vector embedding
- FAISS is used for fast similarity search
- Embeddings are **persisted locally** and reused

---

## 🤖 Question Answering Logic

1. Retrieve top-k relevant chunks from FAISS
2. Construct a **strict prompt** using only retrieved content
3. Generate an answer using FLAN-T5
4. If answer is missing, return:


---

## 🧠 Conversational Memory

- Short-term memory is maintained using Streamlit session state
- Memory is limited to the current session only

---

## 🖥️ User Interface

- Streamlit-based web application
- Sidebar for website indexing
- Chat interface for asking questions
- Displays conversation history clearly

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/anchalpareek24/website_chatbot
cd website_chatbot
```


### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application
```bash
streamlit run app.py
```

## example_usage:
  input:
    website_url: "https://docs.python.org/3/tutorial/controlflow.html"
    user_question: "What is indentation in Python?"
  output:
    chatbot_response: "Indentation refers to the spaces at the beginning of a code line in Python."

## Limitation
- Only the provided URL is indexed (no recursive crawling)

- JavaScript-heavy websites may not be supported

- Large websites may increase indexing time


## Future Improvements
- Recursive crawling of internal links

- Source citation per answer

- Multi-URL support

- Deployment on Streamlit Cloud

## 👤 Author

**Priyanshi Ka. Patel**  
M.Tech in ICT (Machine Learning)  
AI/ML Engineer Candidate



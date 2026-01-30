import streamlit as st

from scraper import scrape_website
from text_processor import chunk_text
from embeddings import create_vectorstore
from qa import get_qa_answer

st.set_page_config(page_title="Website Chatbot", layout="wide")
st.title("🌐 Website-based Chatbot")

# Session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.header("Index Website")
    url = st.text_input("Enter website URL")

    if st.button("Index Website"):
        with st.spinner("Crawling and indexing website..."):
            text = scrape_website(url)

            if not text:
                st.error("Invalid or unreachable website.")
            else:
                chunks = chunk_text(text)
                st.session_state.vectorstore = create_vectorstore(chunks)
                st.session_state.chat_history = []
                st.success("Website indexed successfully!")

# Chat Interface
st.subheader("Ask Questions")

question = st.text_input("Your question")

if question:
    if st.session_state.vectorstore is None:
        st.warning("Please index a website first.")
    else:
        answer = get_qa_answer(st.session_state.vectorstore, question)
        st.session_state.chat_history.append((question, answer))

# Display chat history
for q, a in st.session_state.chat_history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
    st.markdown("---")

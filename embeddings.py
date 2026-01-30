import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

VECTORSTORE_PATH = "data/vectorstore"

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    vectorstore = FAISS.from_texts(chunks, embeddings)

    os.makedirs(VECTORSTORE_PATH, exist_ok=True)
    vectorstore.save_local(VECTORSTORE_PATH)

    return vectorstore


if __name__ == "__main__":
    sample_chunks = [
        "Machine learning is a subset of artificial intelligence.",
        "Supervised learning uses labeled data."
    ]

    vs = create_vectorstore(sample_chunks)
    print("Vectorstore created successfully")

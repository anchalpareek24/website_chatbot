from transformers import pipeline

def get_qa_answer(vectorstore, question):
    """
    Retrieves relevant chunks and generates an answer
    strictly from website content.
    """

    # 1. Retrieve relevant documents
    docs = vectorstore.similarity_search(question, k=3)

    if not docs:
        return "The answer is not available on the provided website."

    context = "\n\n".join([doc.page_content for doc in docs])

    # 2. Strict prompt 
    prompt = f"""
You are a website-based assistant.

Answer the question ONLY using the context below.
If the answer is not present, reply exactly with:
"The answer is not available on the provided website."

Context:
{context}

Question:
{question}

Answer:
"""

    # 3. LLM 
    llm = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=256
    )

    response = llm(prompt)[0]["generated_text"].strip()

    if not response:
        return "The answer is not available on the provided website."

    return response


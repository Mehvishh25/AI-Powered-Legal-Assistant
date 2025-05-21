import streamlit as st
from rag_pipeline import answer_query, llm_model
from vector_handler import process_uploaded_pdf

def run():
    st.markdown(
        "<h1 style='font-size:50px;background: linear-gradient(to right, #0B3D2E, #4CAF50);"
        "-webkit-background-clip: text;-webkit-text-fill-color: transparent;'>PDF Question Answer</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='color:#0B3D2E;'>Ask questions based only on your uploaded legal document.</h3>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='font-size:17px;color:#333;'>"
        "Upload a legal PDF and ask your question. Our AI will answer using only the contents of your document."
        "</p>", unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "📤 Upload a Legal PDF",
        type=["pdf"],
        help="Only .pdf files are supported."
    )

    user_query = st.text_area(
        "💬 Enter your legal question:",
        placeholder="e.g. What are the key clauses in this contract?",
        height=180
    )

    if st.button("🔍 Ask LegalHawk"):
        if uploaded_file:
            st.markdown("<hr>", unsafe_allow_html=True)
            st.chat_message("User").write(user_query)

            # Process the uploaded PDF and generate vector database
            db = process_uploaded_pdf(uploaded_file)

            # Run retrieval-augmented generation
            retrieved_docs = db.similarity_search(user_query)
            response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

            st.chat_message("AI Lawyer").write(response)
        else:
            st.error("⚠️ Please upload a PDF file before asking a question.")

if __name__ == "__main__":
    run()

import streamlit as st
from pypdf import PdfReader
from pdf2image import convert_from_bytes
import pytesseract
from langdetect import detect
import re

def run():
    # Custom styles matching chatbot green theme
    st.markdown("""
        <style>
            .main {
                background-color: #f0fdf4;
                color: #065f46;
            }
            h1, h2, h3, h4, h5 {
                color: #065f46 !important;
            }
            .stButton>button {
                background-color: #10b981;
                color: white;
                border-radius: 8px;
                padding: 8px 20px;
                font-weight: 600;
            }
            .stButton>button:hover {
                background-color: #059669;
            }
            .stTextInput>div>div>input, .stTextArea>div>textarea {
                background-color: #ecfdf5;
                border: 1px solid #10b981;
                color: #065f46;
            }
            .keyword-highlight {
                background-color: #bbf7d0;
                color: #064e3b;
                padding: 4px 8px;
                border-radius: 5px;
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("📄 Legal Document Summarizer")
    st.markdown("Upload a legal document (PDF or TXT) or paste content below. The AI will summarize it and highlight important clauses.")

    summary_length = st.selectbox("📏 Select summary length", ["short", "medium", "long"])
    length_map = {
        "short": {"max_length": 60, "min_length": 20},
        "medium": {"max_length": 120, "min_length": 50},
        "long": {"max_length": 200, "min_length": 80},
    }

    uploaded_file = st.file_uploader("📁 Upload a PDF or TXT file", type=["pdf", "txt"])
    input_text = st.text_area("📌 Or paste your text here", height=200)

    if st.button("Summarize"):
        text = ""

        if uploaded_file:
            if uploaded_file.name.endswith(".pdf"):
                pdf = PdfReader(uploaded_file)
                for page in pdf.pages:
                    content = page.extract_text()
                    if content and filter_non_english_pages(content):
                        text += content
                if not text:
                    st.warning("Extracting text via OCR...")
                    images = convert_from_bytes(uploaded_file.read())
                    for img in images:
                        text += pytesseract.image_to_string(img)
            elif uploaded_file.name.endswith(".txt"):
                text = uploaded_file.read().decode("utf-8")

        elif input_text.strip():
            text = input_text.strip()

        else:
            st.warning("⚠️ Please upload a file or paste some text.")
            return

        # Simple chunk and summary (basic for demo)
        chunks = chunk_text(text)
        summarized_text = ""
        for chunk in chunks:
            # Basic: first 3 sentences per chunk
            sentences = chunk.split(". ")
            summary = ". ".join(sentences[:3]) + ". "
            summarized_text += summary

        st.subheader("📝 Summary")
        st.write(summarized_text)

        st.subheader("📌 Important Clauses")
        keywords = ["termination", "liability", "jurisdiction", "confidentiality", "indemnity", "governing law", "dispute", "arbitration", "payment", "intellectual property"]
        clauses = extract_clauses(text, keywords)
        if not clauses:
            st.write("No key clauses detected (basic scan).")
        else:
            for clause, points in clauses.items():
                st.markdown(f"<span class='keyword-highlight'>🔖 {clause.capitalize()}</span>", unsafe_allow_html=True)
                for sent in points:
                    st.write(f"- {sent}")

def chunk_text(text, chunk_size=1000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def filter_non_english_pages(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def extract_clauses(text, keywords):
    clauses = {kw: [] for kw in keywords}
    sentences = re.split(r'(?<=[.!?]) +', text)
    for sentence in sentences:
        for kw in keywords:
            if kw in sentence.lower():
                clauses[kw].append(sentence.strip())
    return {k: v for k, v in clauses.items() if v}

if __name__ == "__main__":
    run()

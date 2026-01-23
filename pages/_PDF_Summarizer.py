import streamlit as st
from pypdf import PdfReader
from transformers import pipeline

st.title("📄 PDF Notes Summarizer")

@st.cache_resource
def load_sum():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summ = load_sum()

file = st.file_uploader("Upload PDF", type="pdf")

if file:
    reader = PdfReader(file)
    text = "".join(p.extract_text() for p in reader.pages)

    if st.button("Summarize"):
        res = summ(text[:3000], max_length=200, min_length=80)
        st.success(res[0]["summary_text"])

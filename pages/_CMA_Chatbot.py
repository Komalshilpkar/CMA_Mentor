import streamlit as st
import os
import json
from groq import Groq

# ---------------- PAGE ----------------
st.title("🤖 CMA  Mentor")

# ---------------- GROQ CLIENT ----------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def ask_groq(question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior CMA faculty member. "
                    "Give detailed, exam-oriented answers with examples and tips."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.6
    )
    return response.choices[0].message.content

# ---------------- LOAD SYLLABUS ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYLLABUS_PATH = os.path.join(BASE_DIR, "data", "cma_syllabus.json")

with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
    SYLLABUS = json.load(f)

# ---------------- BUILD SYLLABUS KEYWORDS ----------------
def build_keywords(syllabus):
    keys = set()
    for level in syllabus.values():
        for paper in level.values():
            keys.update(paper["name"].lower().split())
            for sec in paper["sections"]:
                keys.update(sec.lower().split())
    keys.update([
        "brs", "bank reconciliation", "marginal costing",
        "budgetary control", "variance analysis",
        "cost accounting", "management accounting",
        "financial accounting", "gst", "direct tax"
    ])
    return keys

SYLLABUS_KEYS = build_keywords(SYLLABUS)

def is_cma_question(q):
    q = q.lower()
    return any(k in q for k in SYLLABUS_KEYS)

# ---------------- UI ----------------
question = st.text_area("Ask your CMA question")

# ---------------- MAIN LOGIC ----------------
if st.button("Ask Mentor"):

    if not question.strip():
        st.warning("Please enter a question")
        st.stop()

    if not is_cma_question(question):
        st.warning("Answering in CMA exam context")

    with st.spinner("Thinking like a CMA faculty..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a senior CMA faculty member. "
                        "Answer all questions in CMA exam-oriented manner. "
                        "Give detailed explanations with examples, reasons, "
                        "and exam tips. Write like a human teacher."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.6
        )

    answer = response.choices[0].message.content

    st.caption("ℹ️ Answer generated using GPT model with CMA exam standards.")
    st.success(answer)








# import streamlit as st
# import json
# import os
# from transformers import pipeline
# from duckduckgo_search import DDGS

# # ---------------- WEB SEARCH FUNCTION ----------------



# def web_search(query, max_results=5):
#     # ---- sanitize input ----
#     if not query or not query.strip():
#         return ""

#     query = query.strip()

#     results = []
#     try:
#         with DDGS() as ddgs:
#             for r in ddgs.text(keywords=query, max_results=max_results):
#                 if isinstance(r, dict) and "body" in r:
#                     results.append(r["body"])
#     except Exception:
#         # fail gracefully
#         return ""

#     return "\n".join(results)



# # ---------------- PAGE TITLE ----------------
# st.title("🤖 CMA AI Mentor (Accurate & Syllabus-Based)")
# question = st.text_area("Ask your CMA question")
# mode = st.radio(
#     "Answer Mode",
#     [
#         "CMA Syllabus (Safe)",
#         "Live Web (ChatGPT-like)"
#     ],
#     help="Choose syllabus-safe mode or live web search mode"
# )


# if mode == "Live Web (ChatGPT-like)":
#     with st.spinner("Searching live data..."):
#         web_data = web_search(question)
#         if not web_data:
#             st.warning("⚠️ Live data unavailable. Answering from general knowledge.")

# elif mode == "Live Web (ChatGPT-like)":
#     with st.spinner("Searching live data..."):
#         web_data = web_search(question)

#     prompt = f"""
# You are an expert CMA faculty member.

# Answer the question strictly as per CMA exam standards.
# Your answer MUST include:

# 1. Clear definition
# 2. Explanation in simple language
# 3. Reasons / objectives (where applicable)
# 4. Practical or exam relevance
# 5. Example or points if relevant
# 6. Short exam tips (if applicable)

# Write the answer in a structured, detailed format.
# Do NOT give a one-line answer.

# CMA Reference Notes:
# {knowledge}

# Question:
# {question}

# Answer:
# """


# #     prompt = f"""
# # You are a CMA mentor.

# # Use the following LIVE DATA to answer clearly and accurately.
# # Stick to CMA syllabus concepts.

# # Live Data:
# # {web_data}

# # Question:
# # {question}

# # Answer:
# # """
# #     response = llm(prompt)
# #     st.success(response[0]["generated_text"])



# # ---------------- PATH HANDLING (ROBUST) ----------------
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_DIR = os.path.join(BASE_DIR, "data")

# KNOWLEDGE_PATH = os.path.join(DATA_DIR, "cma_knowledge.txt")
# YOUTUBE_PATH = os.path.join(DATA_DIR, "youtube_cma.json")

# # ---------------- LOAD CMA KNOWLEDGE ----------------
# try:
#     with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
#         knowledge = f.read()
# except FileNotFoundError:
#     knowledge = ""
#     st.error("❌ cma_knowledge.txt not found in data folder")

# # ---------------- LOAD YOUTUBE DATA ----------------
# try:
#     with open(YOUTUBE_PATH, "r", encoding="utf-8") as f:
#         yt_data = json.load(f)
# except FileNotFoundError:
#     yt_data = {}
#     st.warning("⚠️ youtube_cma.json not found. YouTube suggestions disabled.")




# # ---------------- LOAD LLM ----------------
# @st.cache_resource
# def load_llm():
#     return pipeline(
#         "text2text-generation",
#         model="google/flan-t5-base",
#         max_length=512
#     )

# llm = load_llm()

# # ---------------- HELPERS ----------------
# def is_cma_question(q):
#     keywords = [
#         "cost", "costing", "budget", "marginal",
#         "break even", "tax", "law",
#         "financial", "brs", "bank reconciliation"
#     ]
#     return any(k in q.lower() for k in keywords)

# def find_topic(q):
#     q = q.lower()
#     for topic in yt_data.keys():
#         if topic in q:
#             return topic
#     return None

# # ---------------- UI ----------------
# # question = st.text_area("Ask your CMA question")

# if st.button("Ask Mentor"):
#     if not question.strip():
#         st.warning("Please enter a question")
#         st.stop()

#     if not is_cma_question(question):
#         st.error("❌ This question is outside the CMA syllabus")
#         st.stop()

#     # ---------- SAFE MODE ----------
#     if mode == "CMA Syllabus (Safe)":
#         prompt = f"""
# You are a CMA mentor.

# Answer the question strictly as per CMA exam standards.

# Instructions:
# - First, use the CMA reference notes if relevant
# - If exact content is not present, answer using your CMA subject knowledge
# - DO NOT say "not covered yet"
# - Provide a full, structured exam-oriented answer

# Your answer MUST include:
# 1. Definition
# 2. Explanation
# 3. Reasons / objectives
# 4. Exam relevance
# 5. Example (if applicable)
# 6. Exam tips

# CMA Reference Notes (if useful):
# {knowledge}


# CMA Notes:
# {knowledge}

# Question:
# {question}

# Answer:
# """
#         response = llm(prompt)

#         st.caption("ℹ️ Answer generated using CMA syllabus knowledge and exam standards.")

#         st.success(response[0]["generated_text"])

#     # ---------- LIVE WEB MODE ----------
#     elif mode == "Live Web (ChatGPT-like)":
#         with st.spinner("Searching live data..."):
#             web_data = web_search(question)

#         prompt = f"""
# You are a CMA mentor.

# Use the LIVE DATA below to answer clearly.
# Stick to CMA syllabus concepts.

# Live Data:
# {web_data}

# Question:
# {question}

# Answer:
# """
#         response = llm(prompt)
#         st.success(response[0]["generated_text"])


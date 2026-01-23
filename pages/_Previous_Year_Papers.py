import streamlit as st
from groq import Groq

# ---------------- PAGE ----------------
st.title("📜 CMA Previous Year Papers")

st.caption(
    "Generate CMA Previous Year Paper–style questions using AI. "
    "These are PYQ-pattern questions created based on historical CMA exams."
)

# ---------------- GROQ CLIENT ----------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---------------- USER INPUT ----------------
level = st.selectbox(
    "Select CMA Level",
    ["Foundation", "Intermediate", "Final"]
)

year = st.selectbox(
    "Select Exam Year (for pattern reference)",
    ["2024", "2023", "2022", "2021", "2020"]
)

paper = st.text_input(
    "Enter Paper Name / Subject",
    placeholder="e.g. Cost Accounting, Management Accounting"
)

custom_instruction = st.text_input(
    "Any specific instruction? (Optional)",
    placeholder=(
        "Examples:\n"
        "• Generate numerical-heavy paper\n"
        "• Focus on frequently repeated CMA questions\n"
        "• Include theory + numericals\n"
        "• Tough paper like real exam"
    )
)

# ---------------- AI GENERATOR ----------------
def generate_ai_pyq(level, year, paper, instruction):
    prompt = f"""
You are a senior CMA examiner.

Generate a FULL CMA Previous Year Question Paper–style set.

Exam Details:
- CMA Level: {level}
- Exam Year Pattern Reference: {year}
- Paper: {paper}

User Instruction:
{instruction if instruction.strip() else "Standard CMA exam pattern."}

Rules:
- Follow real CMA exam difficulty
- Use PYQ-style wording
- Mix theory and numerical questions
- Avoid MCQs unless CMA pattern includes them
- Write questions exactly like an exam paper

FORMAT:

SECTION A
(Answer any X questions)
1. ...
2. ...

SECTION B
(Answer any Y questions)
3. ...
4. ...

SECTION C
(Long answer / numerical)
5. ...
6. ...

Do NOT provide answers. Only questions.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert CMA question paper setter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# ---------------- GENERATE PAPER ----------------
if st.button("Generate AI Previous Year Paper"):

    if not paper.strip():
        st.warning("Please enter paper name / subject.")
        st.stop()

    with st.spinner("Generating CMA Previous Year Paper (AI)…"):
        paper_text = generate_ai_pyq(level, year, paper, custom_instruction)

    st.caption("ℹ️ This is an AI-generated PYQ-style paper based on CMA exam patterns.")
    st.subheader("📄 AI Generated Previous Year Paper")
    st.markdown(paper_text)

    # st.text_area("📄 AI Generated Previous Year Paper", paper_text, height=450)










# import streamlit as st
# import os
# from groq import Groq

# # ---------------- PAGE TITLE ----------------
# st.title("📚 CMA Previous Year Papers – AI Assistant")

# st.caption(
#     "Interact with CMA Previous Year Papers using AI. "
#     "Ask explanations, generate mock tests, PYQ-style MCQs, summaries, or anything you want."
# )

# # ---------------- GROQ CLIENT ----------------
# client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# # ---------------- BASE PATH ----------------
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PYQ_BASE = os.path.join(BASE_DIR, "data", "previous_year_papers")

# # ---------------- USER SELECTION ----------------
# level = st.selectbox(
#     "Select CMA Level",
#     ["Foundation", "Intermediate", "Final"]
# )

# level_path = os.path.join(PYQ_BASE, level)

# if not os.path.exists(level_path):
#     st.warning("No previous year papers uploaded for this level.")
#     st.stop()

# years = sorted(os.listdir(level_path), reverse=True)
# year = st.selectbox("Select Year", years)

# year_path = os.path.join(level_path, year)

# papers = [f for f in os.listdir(year_path) if f.endswith(".txt")]

# paper = st.selectbox("Select Paper", papers)

# # ---------------- LOAD PAPER CONTENT ----------------
# paper_path = os.path.join(year_path, paper)

# with open(paper_path, "r", encoding="utf-8") as f:
#     paper_content = f.read()

# st.subheader("📄 Paper Content Preview")
# st.text_area("Previous Year Questions", paper_content, height=220)

# # ---------------- USER QUERY ----------------
# user_instruction = st.text_area(
#     "Ask anything about this paper (AI-powered)",
#     placeholder=(
#         "Examples:\n"
#         "• Explain Question 2 step by step\n"
#         "• Generate 10 MCQs from this paper\n"
#         "• Ask PYQ-style tricky MCQs\n"
#         "• Summarize important topics for exam\n"
#         "• Convert this paper into a mock test"
#     )
# )

# # ---------------- AI FUNCTION ----------------
# def ask_pyq_ai(paper_text, instruction):
#     prompt = f"""
# You are a senior CMA faculty member.

# You are given a CMA Previous Year Question Paper.

# Paper Content:
# {paper_text}

# User Request:
# {instruction}

# Instructions:
# - Answer strictly in CMA exam context
# - Give clear, detailed, structured answers
# - If MCQs are asked, generate CMA-level MCQs
# - If explanation is asked, explain step by step
# - Be exam-oriented and practical

# Answer:
# """

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {"role": "system", "content": "You are an expert CMA examiner and teacher."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.6
#     )

#     return response.choices[0].message.content


# # ---------------- PROCESS QUERY ----------------
# if st.button("Ask AI about this Paper"):

#     if not user_instruction.strip():
#         st.warning("Please enter your question or instruction.")
#         st.stop()

#     with st.spinner("Analyzing previous year paper..."):
#         answer = ask_pyq_ai(paper_content, user_instruction)

#     st.caption("ℹ️ Answer generated using free Groq LLaMA-3.1 model (PYQ-aware).")
#     st.success(answer)










# import streamlit as st
# import os

# st.title(" CMA Previous Year Question Papers")

# # ---------------- BASE PATH ----------------
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PYQ_BASE = os.path.join(BASE_DIR, "data", "previous_year_papers")

# # ---------------- SELECT CMA LEVEL ----------------
# level = st.selectbox(
#     "Select CMA Level",
#     ["Foundation", "Intermediate", "Final"]
# )

# level_path = os.path.join(PYQ_BASE, level)

# if not os.path.exists(level_path):
#     st.warning("No papers uploaded for this level yet.")
#     st.stop()

# # ---------------- SELECT YEAR ----------------
# years = sorted(os.listdir(level_path), reverse=True)

# if not years:
#     st.warning("No year-wise papers found.")
#     st.stop()

# year = st.selectbox("Select Year", years)

# year_path = os.path.join(level_path, year)

# # ---------------- LIST PAPERS ----------------
# papers = [f for f in os.listdir(year_path) if f.endswith(".pdf")]

# if not papers:
#     st.warning("No papers available for selected year.")
#     st.stop()

# st.subheader(f" {level} – {year} Papers")

# for paper in papers:
#     paper_path = os.path.join(year_path, paper)

#     with open(paper_path, "rb") as f:
#         st.download_button(
#             label=f"⬇ Download {paper}",
#             data=f,
#             file_name=paper,
#             mime="application/pdf"
#         )

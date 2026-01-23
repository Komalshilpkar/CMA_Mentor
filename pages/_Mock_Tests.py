import streamlit as st
import random
from groq import Groq

# ---------------- PAGE TITLE ----------------
st.title("📝 CMA Mock Test")

st.caption(
    "Generate CMA-level mock tests using AI. "
    "You can also give custom instructions like numericals only, PYQ style, tricky questions, etc."
)

# ---------------- GROQ CLIENT ----------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---------------- USER INPUTS ----------------
level = st.selectbox(
    "Select CMA Level",
    ["Foundation", "Intermediate", "Final"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

topic = st.text_input(
    "Enter CMA Topic",
    placeholder="e.g. Bank Reconciliation Statement, Marginal Costing"
)

custom_instruction = st.text_area(
    "Any specific instruction? (Optional)",
    placeholder=(
        "Examples:\n"
        "• Ask numerical questions only\n"
        "• PYQ-style tricky MCQs\n"
        "• Conceptual theory questions\n"
        "• CMA exam trap questions"
    )
)

# ---------------- AI QUESTION GENERATOR ----------------
def generate_mcq_groq(level, topic, difficulty, instruction):
    prompt = f"""
You are a senior CMA examiner.

Generate ONE HIGH-QUALITY CMA MCQ.

Exam Details:
- CMA Level: {level}
- Difficulty: {difficulty}
- Topic: {topic}

User Instruction (must be followed if provided):
{instruction if instruction.strip() else "No special instruction. Use standard CMA exam pattern."}

Rules:
- Question must be strictly CMA syllabus-relevant
- Avoid repetition
- Options must be realistic and exam-oriented
- Follow the instruction carefully

FORMAT STRICTLY AS:

Question:
<question text>

A. <option A>
B. <option B>
C. <option C>
D. <option D>

Correct Answer:
<write option letter only>

Explanation:
<short CMA exam explanation>
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an experienced CMA paper setter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# ---------------- GENERATE MOCK TEST ----------------
if st.button("Generate Mock Test"):

    if not topic.strip():
        st.warning("Please enter a CMA topic")
        st.stop()

    st.session_state["test"] = []

    with st.spinner("Generating 20 CMA-level questions…"):
        for i in range(1, 21):
            try:
                raw = generate_mcq_groq(level, topic, difficulty, custom_instruction)

                q_text = raw.split("Question:")[1].split("A.")[0].strip()

                options_block = raw.split("A.")[1].split("Correct Answer:")[0]
                option_lines = [o.strip() for o in options_block.split("\n") if o.strip()]

                options = {
                    "A": option_lines[0][3:].strip(),
                    "B": option_lines[1][3:].strip(),
                    "C": option_lines[2][3:].strip(),
                    "D": option_lines[3][3:].strip(),
                }

                correct = raw.split("Correct Answer:")[1].split("Explanation:")[0].strip()
                explanation = raw.split("Explanation:")[1].strip()

                st.session_state["test"].append({
                    "question": f"Q{i}. {q_text}",
                    "options": options,
                    "answer": correct,
                    "explanation": explanation
                })

            except Exception:
                continue


# ---------------- DISPLAY MOCK TEST ----------------
if "test" in st.session_state and len(st.session_state["test"]) > 0:

    st.subheader("📘 CMA Mock Test")

    user_answers = {}
    score = 0

    for i, q in enumerate(st.session_state["test"]):
        st.markdown(f"**{q['question']}**")

        choice = st.radio(
            "Choose answer",
            list(q["options"].keys()),
            format_func=lambda x: f"{x}. {q['options'][x]}",
            key=f"q_{i}"
        )
        user_answers[i] = choice

    if st.button("Submit Test"):

        st.subheader("📊 Results & Explanations")

        for i, q in enumerate(st.session_state["test"]):
            if user_answers.get(i) == q["answer"]:
                score += 1
                st.success(f"✅ {q['question']}")
            else:
                st.error(f"❌ {q['question']}")

            st.markdown(f"**Correct Answer:** {q['answer']}")
            st.info(f"📘 Explanation: {q['explanation']}")
            st.markdown("---")

        st.success(f"🎯 Final Score: {score} / 20")

        if score >= 14:
            st.balloons()
            st.success("✅ Exam-Ready Level")
        else:
            st.warning("⚠️ Needs More Practice")












# import streamlit as st
# from transformers import pipeline
# import json
# import random
# import os

# st.title("📝 AI-Based CMA Mock Test (Advanced)")

# # ---------------- PATH & SYLLABUS LOAD ----------------
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SYLLABUS_PATH = os.path.join(BASE_DIR, "data", "cma_syllabus.json")

# # with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
# #     SYLLABUS = json.load(f)

# if not os.path.exists(SYLLABUS_PATH):
#     st.error("❌ cma_syllabus.json not found in data folder")
#     st.stop()

# with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
#     SYLLABUS = json.load(f)


# # ---------------- LLM ----------------
# @st.cache_resource
# def load_llm():
#     return pipeline(
#         "text2text-generation",
#         model="google/flan-t5-base",
#         do_sample=True,
#         temperature=0.8,
#         top_p=0.9,
#         max_length=200
#     )

# llm = load_llm()

# # ---------------- USER INPUT (AUTO FROM SYLLABUS) ----------------
# level = st.selectbox("Select CMA Level", list(SYLLABUS.keys()))

# paper = st.selectbox(
#     "Select Paper",
#     list(SYLLABUS[level].keys())
# )

# section = st.selectbox(
#     "Select Section",
#     list(SYLLABUS[level][paper]["sections"].keys())
# )

# difficulty = st.selectbox(
#     "Select Difficulty",
#     ["Easy", "Medium", "Hard"]
# )

# # ---------------- QUESTION TYPES ----------------
# QUESTION_TYPES = [
#     "definition",
#     "concept",
#     "application",
#     "purpose",
#     "difference",
#     "procedure",
#     "true_false"
# ]

# # ---------------- GENERATE ONE QUESTION ----------------
# def generate_question(level, paper, section, difficulty, q_type):
#     prompt = f"""
# You are a CMA examiner.

# Generate ONE CMA MCQ.

# CMA Level: {level}
# Paper: {paper} - {SYLLABUS[level][paper]['name']}
# Section: {section}
# Difficulty: {difficulty}
# Question Type: {q_type}

# Return STRICTLY in this format:

# Question:
# <question text>

# Correct Answer:
# <one short correct statement>

# Wrong Options:
# <option 1>
# <option 2>
# <option 3>

# Explanation:
# <short exam-oriented explanation>
# """
#     return llm(prompt)[0]["generated_text"]

# # ---------------- GENERATE MOCK TEST ----------------
# if st.button("Generate Mock Test"):
#     st.session_state["test"] = []

#     with st.spinner("Generating 20 CMA-level questions..."):
#         for i in range(1, 21):
#             q_type = random.choice(QUESTION_TYPES)
#             raw = generate_question(level, paper, section, difficulty, q_type)

#             try:
#                 q_text = raw.split("Question:")[1].split("Correct Answer:")[0].strip()
#                 correct = raw.split("Correct Answer:")[1].split("Wrong Options:")[0].strip()
#                 wrong_block = raw.split("Wrong Options:")[1].split("Explanation:")[0]
#                 wrongs = [w.strip() for w in wrong_block.split("\n") if w.strip()]
#                 explanation = raw.split("Explanation:")[1].strip()

#                 options = wrongs[:3] + [correct]
#                 random.shuffle(options)

#                 st.session_state["test"].append({
#                     "level": level,
#                     "paper": paper,
#                     "section": section,
#                     "question": f"Q{i}. {q_text}",
#                     "options": options,
#                     "answer": correct,
#                     "explanation": explanation
#                 })

#             except Exception:
#                 continue

# # ---------------- DISPLAY TEST ----------------
# if "test" in st.session_state and len(st.session_state["test"]) > 0:
#     st.subheader("📘 Mock Test")

#     user_answers = {}
#     score = 0

#     for i, q in enumerate(st.session_state["test"]):
#         st.markdown(f"**{q['question']}**")

#         choice = st.radio(
#             "Choose answer",
#             q["options"],
#             key=f"q_{i}"
#         )
#         user_answers[i] = choice

#     if st.button("Submit Test"):
#         st.subheader("📊 Results & Explanations")

#         st.session_state.setdefault("analytics", [])

#         for i, q in enumerate(st.session_state["test"]):
#             correct = user_answers[i] == q["answer"]

#             st.session_state["analytics"].append({
#                 "level": q["level"],
#                 "paper": q["paper"],
#                 "section": q["section"],
#                 "correct": correct
#             })

#             if correct:
#                 score += 1
#                 st.success(f"✅ {q['question']}")
#             else:
#                 st.error(f"❌ {q['question']}")

#             st.markdown(f"**Correct Answer:** {q['answer']}")
#             st.info(f"📘 Explanation: {q['explanation']}")
#             st.markdown("---")

#         st.success(f"🎯 Final Score: {score} / 20")

#         if score >= 14:
#             st.balloons()
#             st.success("✅ Exam Ready Level")
#         else:
#             st.warning("⚠️ Needs More Practice")






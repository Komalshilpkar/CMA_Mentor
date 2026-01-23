import streamlit as st
import os, json, random
import pandas as pd
import plotly.express as px
from groq import Groq
from pypdf import PdfReader
from transformers import pipeline

# -------------------------------------------------
# CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="CMA AI Mentor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# LOGIN
# -------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 CMA AI Mentor Login")
    st.caption("Demo → Username: admin | Password: admin")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if u == "admin" and p == "admin":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "CMA Chatbot",
        "CMA Syllabus",
        "Mock Tests",
        "PDF Summarizer",
        "Performance",
        "Previous Year Papers",
        "Study Planner",
    ]
)

st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# -------------------------------------------------
# GROQ CLIENT
# -------------------------------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# =================================================
# DASHBOARD
# =================================================
if menu == "Dashboard":
    st.title("🏠 Dashboard")

    c1, c2, c3 = st.columns(3)
    c1.metric("Subjects", "6")
    c2.metric("Study Hours", "4")
    c3.metric("Readiness", "72%")

    df = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri"],
        "Hours": [2,3,4,3,5]
    })
    st.line_chart(df.set_index("Day"))

# =================================================
# CMA CHATBOT
# =================================================
elif menu == "CMA Chatbot":
    st.title("🤖 CMA Mentor")

    question = st.text_area("Ask your CMA question")

    if st.button("Ask Mentor") and question.strip():
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role":"system","content":"You are a senior CMA faculty member. Give detailed exam-oriented answers."},
                {"role":"user","content":question}
            ],
            temperature=0.6
        )
        st.success(response.choices[0].message.content)

# =================================================
# CMA SYLLABUS
# =================================================
elif menu == "CMA Syllabus":

    st.title("📘 CMA Syllabus (Official)")

    level = st.selectbox(
        "Select CMA Level",
        ["Foundation", "Intermediate", "Final"]
    )

    # ================= FOUNDATION =================
    if level == "Foundation":
        st.subheader("CMA Foundation Course (Total Marks: 400)")

        st.markdown("""
### 📄 Paper 1: Fundamentals of Business Laws & Business Communication (FBLC)
- Section A: Fundamentals of Business Laws – **80%**
- Section B: Business Communication – **20%**

### 📄 Paper 2: Fundamentals of Financial & Cost Accounting (FFCA)
- Section A: Fundamentals of Financial Accounting – **70%**
- Section B: Fundamentals of Cost Accounting – **30%**

### 📄 Paper 3: Fundamentals of Business Mathematics & Statistics (FBMS)
- Section A: Business Mathematics – **40%**
- Section B: Business Statistics – **60%**

### 📄 Paper 4: Fundamentals of Business Economics & Management (FBEM)
- Section A: Business Economics – **70%**
- Section B: Fundamentals of Management – **30%**

📌 *Each paper carries 100 marks*
""")

    # ================= INTERMEDIATE =================
    elif level == "Intermediate":
        st.subheader("CMA Intermediate Course (Total Marks: 800)")

        st.markdown("""
## 🔹 Group I

### 📄 Paper 5: Business Laws & Ethics (BLE)
- Business Laws – **30%**
- Industrial Laws – **15%**
- Corporate Laws – **40%**
- Business Ethics – **15%**

### 📄 Paper 6: Financial Accounting (FA)
- Accounting Fundamentals – **15%**
- Special Transactions – **10%**
- Financial Statements – **20%**
- Partnership Accounts – **20%**
- Lease, Branch & Dept. Accounts – **15%**
- Accounting Standards – **20%**

### 📄 Paper 7: Direct & Indirect Taxation (DITX)
- Direct Taxation – **50%**
- Indirect Taxation – **50%**

### 📄 Paper 8: Cost Accounting (CA)
- Introduction to Cost Accounting – **40%**
- Methods of Costing – **30%**
- Cost Accounting Techniques – **30%**

## 🔹 Group II

### 📄 Paper 9: Operations & Strategic Management (OMSM)
- Operations Management – **60%**
- Strategic Management – **40%**

### 📄 Paper 10: Corporate Accounting & Auditing (CAA)
- Corporate Accounting – **50%**
- Auditing – **50%**

### 📄 Paper 11: Financial Management & Business Data Analytics (FMDA)
- Financial Management – **80%**
- Business Data Analytics – **20%**

### 📄 Paper 12: Management Accounting (MA)
- Intro to MA – **5%**
- Activity Based Costing – **10%**
- Decision Making Tools – **30%**
- Standard Costing & Variance Analysis – **15%**
- Budgeting & Budgetary Control – **15%**
- Divisional Performance Measurement – **10%**
- Responsibility Accounting – **5%**
- Decision Theory – **10%**

📌 *Each paper carries 100 marks*
""")

    # ================= FINAL =================
    else:
        st.subheader("CMA Final Course (Total Marks: 800)")

        st.markdown("""
## 🔹 Group III

### 📄 Paper 13: Corporate & Economic Laws (CEL)
- Corporate Laws – **60%**
- Economic Laws & Regulations – **40%**

### 📄 Paper 14: Strategic Financial Management (SFM)
- Investment Decisions – **25%**
- Security Analysis & Portfolio Mgmt – **35%**
- Financial Risk Management – **20%**
- International Financial Management – **15%**
- Digital Finance – **5%**

### 📄 Paper 15: Direct Tax Laws & International Taxation (DIT)
- Direct Tax Laws – **60%**
- International Taxation – **40%**

### 📄 Paper 16: Strategic Cost Management (SCM)
- Strategic Cost Management – **60%**
- Quantitative Techniques – **40%**

## 🔹 Group IV

### 📄 Paper 17: Cost & Management Audit (CMAD)
- Cost Audit – **50%**
- Management Audit – **25%**
- Internal & Operational Audit – **15%**
- Forensic Audit & AML – **10%**

### 📄 Paper 18: Corporate Financial Reporting (CFR)
- Indian Accounting Standards – **25%**
- Valuation & Financial Instruments – **15%**
- Business Combinations – **20%**
- Consolidated Financial Statements – **20%**
- Recent Developments – **10%**
- Government Accounting – **10%**

### 📄 Paper 19: Indirect Tax Laws & Practice (ITLP)
- GST Act & Rules – **70%**
- Customs Act & Rules – **30%**

## 🔹 Elective Papers (Choose ONE)

### 📄 Paper 20A: Strategic Performance Management & Business Valuation
- Strategic Performance Management – **50%**
- Business Valuation – **50%**

### 📄 Paper 20B: Risk Management in Banking & Insurance
- Banking – **60%**
- Insurance – **40%**

### 📄 Paper 20C: Entrepreneurship & Startup
- Entrepreneurial Skills – **15%**
- Ecosystem – **15%**
- Idea to Action – **15%**
- Value Addition – **15%**
- Scale Up – **10%**
- Risk Management – **10%**
- Leadership – **10%**
- New Age Business – **10%**

📌 *Each paper carries 100 marks*
""")


# =================================================
# MOCK TESTS
# =================================================
elif menu == "Mock Tests":
    st.title("📝 CMA Mock Tests")

    level = st.selectbox("Level", ["Foundation","Intermediate","Final"])
    difficulty = st.selectbox("Difficulty", ["Easy","Medium","Hard"])
    topic = st.text_input("Topic")

    if st.button("Generate Mock Test") and topic:
        raw = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role":"system","content":"You are a CMA examiner."},
                {"role":"user","content":f"Generate 5 CMA MCQs on {topic} with answers and explanations."}
            ]
        )
        st.markdown(raw.choices[0].message.content)

# =================================================
# PDF SUMMARIZER
# =================================================
elif menu == "PDF Summarizer":
    st.title("📄 PDF Summarizer")

    @st.cache_resource
    def load_sum():
        return pipeline("summarization", model="facebook/bart-large-cnn")

    summ = load_sum()
    file = st.file_uploader("Upload PDF", type="pdf")

    if file and st.button("Summarize"):
        reader = PdfReader(file)
        text = "".join(p.extract_text() for p in reader.pages)
        res = summ(text[:3000], max_length=200, min_length=80)
        st.success(res[0]["summary_text"])

# =================================================
# PERFORMANCE
# =================================================
elif menu == "Performance":
    st.title("📊 Performance Analytics")

    df = pd.DataFrame({
        "Subject":["Costing","FM","Law"],
        "Score":[65,70,55]
    })
    fig = px.bar(df, x="Subject", y="Score")
    st.plotly_chart(fig)

# =================================================
# PREVIOUS YEAR PAPERS (AI)
# =================================================
elif menu == "Previous Year Papers":
    st.title("📜 AI Previous Year Papers")

    subject = st.text_input("Paper Name")
    if st.button("Generate PYQ") and subject:
        pyq = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role":"system","content":"You are a CMA examiner."},
                {"role":"user","content":f"Generate a CMA PYQ-style paper for {subject}."}
            ]
        )
        st.markdown(pyq.choices[0].message.content)

# =================================================
# STUDY PLANNER
# =================================================
elif menu == "Study Planner":
    st.title("📅 Study Planner")

    hours = st.slider("Daily Study Hours", 1, 10, 4)
    subjects = {"Costing":0.25,"FM":0.2,"Law":0.15,"DT":0.2,"IDT":0.2}

    if st.button("Generate Plan"):
        plan = {s: round(hours*w,2) for s,w in subjects.items()}
        st.dataframe(pd.DataFrame(plan.items(), columns=["Subject","Hours"]))







# import streamlit as st

# st.set_page_config(
#     page_title="CMA AI Mentor",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ---------------- SESSION ----------------
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # ---------------- LOGIN PAGE ----------------
# if not st.session_state.logged_in:
#     st.title("🔐 CMA AI Mentor Login")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "admin":
#             st.session_state.logged_in = True
#             st.success("Login successful!")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")

# # ---------------- MAIN APP AFTER LOGIN ----------------
# else:
#     st.sidebar.title("📚 CMA AI Mentor")

#     # 🔗 MANUAL SIDEBAR NAVIGATION
#     st.sidebar.page_link("pages/_Dashboard.py", label="🏠 Dashboard")
#     st.sidebar.page_link("pages/_CMA_Chatbot.py", label="🤖 CMA Chatbot")
#     st.sidebar.page_link("pages/_CMA_Syllabus.py", label="📘 CMA Syllabus")
#     st.sidebar.page_link("pages/_Mock_Tests.py", label="📝 Mock Tests")
#     st.sidebar.page_link("pages/_AI_Previous_Year_Papers.py", label="📜 Previous Year Papers")
#     st.sidebar.page_link("pages/_PDF_Summarizer.py", label="📄 PDF Summarizer")
#     st.sidebar.page_link("pages/_Performance.py", label="📊 Performance")
#     st.sidebar.page_link("pages/_Study_Planner.py", label="📅 Study Planner")

#     st.title("🏠 CMA AI Mentor Dashboard")
#     st.success("Welcome! Use the sidebar to navigate through all features.")

#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()











# import streamlit as st

# st.set_page_config(page_title="CMA AI Mentor", layout="wide")

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# st.title(" CMA Mentor Login")

# if not st.session_state.logged_in:
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "admin":
#             st.session_state.logged_in = True
#             st.success("Login successful!")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")
# else:
#     st.success(" Logged in! Use the sidebar to navigate.")







# import streamlit as st
# from utils.auth import login

# st.set_page_config(page_title="CMA Mentor", page_icon="📘", layout="wide")

# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     st.title(" CMA Mentor Login")
#     login()
#     st.stop()

# st.title("CMA Mentor – AI & ML Powered Learning Platform")
# st.success("Welcome to your personal CMA Mentor")
# st.markdown(
#     "Use the **sidebar** to access syllabus, chatbot, planner, tests, analytics and AI tools."
# )

# import streamlit as st

# st.set_page_config(
#     page_title="CMA AI Mentor",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ---------------- SESSION ----------------
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # ---------------- LOGIN PAGE ----------------
# if not st.session_state.logged_in:
#     st.title("🔐 CMA AI Mentor Login")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "admin":
#             st.session_state.logged_in = True
#             st.success("Login successful!")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")

# # ---------------- MAIN APP AFTER LOGIN ----------------
# else:
#     st.sidebar.title("📚 CMA AI Mentor")

#     # 🔗 MANUAL SIDEBAR NAVIGATION
#     st.sidebar.page_link("pages/_Dashboard.py", label="🏠 Dashboard")
#     st.sidebar.page_link("pages/_CMA_Chatbot.py", label="🤖 CMA Chatbot")
#     st.sidebar.page_link("pages/_CMA_Syllabus.py", label="📘 CMA Syllabus")
#     st.sidebar.page_link("pages/_Mock_Tests.py", label="📝 Mock Tests")
#     st.sidebar.page_link("pages/_AI_Previous_Year_Papers.py", label="📜 Previous Year Papers")
#     st.sidebar.page_link("pages/_PDF_Summarizer.py", label="📄 PDF Summarizer")
#     st.sidebar.page_link("pages/_Performance.py", label="📊 Performance")
#     st.sidebar.page_link("pages/_Study_Planner.py", label="📅 Study Planner")

#     st.title("🏠 CMA AI Mentor Dashboard")
#     st.success("Welcome! Use the sidebar to navigate through all features.")

#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()











# import streamlit as st

# st.set_page_config(page_title="CMA AI Mentor", layout="wide")

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# st.title("🔐 CMA Mentor Login")

# if not st.session_state.logged_in:
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "admin":
#             st.session_state.logged_in = True
#             st.success("Login successful!")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")
# else:
#     st.success("✅ Logged in! Use the sidebar to navigate.")







# import streamlit as st
# from utils.auth import login

# st.set_page_config(page_title="CMA Mentor", page_icon="📘", layout="wide")

# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False

# if not st.session_state["logged_in"]:
#     st.title("📘 CMA Mentor Login")
#     login()
#     st.stop()

# st.title("📘 CMA Mentor – AI & ML Powered Learning Platform")
# st.success("Welcome to your personal CMA Mentor")
# st.markdown(
#     "Use the **sidebar** to access syllabus, chatbot, planner, tests, analytics and AI tools."
# )


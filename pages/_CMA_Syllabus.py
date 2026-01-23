import streamlit as st

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

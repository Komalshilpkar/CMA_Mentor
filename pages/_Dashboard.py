import streamlit as st
import pandas as pd

st.title("🏠 Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Subjects", "6")
col2.metric("Study Hours", "4")
col3.metric("Readiness", "72%")

data = pd.DataFrame({
    "Day": ["Mon","Tue","Wed","Thu","Fri"],
    "Hours": [2,3,4,3,5]
})

st.line_chart(data.set_index("Day"))

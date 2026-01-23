import streamlit as st
import pandas as pd

st.title("📅 Study Planner")

hours = st.slider("Daily Study Hours", 1, 10, 4)

subjects = {
    "Costing": 0.25,
    "FM": 0.20,
    "Law": 0.15,
    "DT": 0.20,
    "IDT": 0.20
}

if st.button("Generate Plan"):
    plan = {s: round(hours*w,2) for s,w in subjects.items()}
    st.dataframe(pd.DataFrame(plan.items(), columns=["Subject","Hours"]))

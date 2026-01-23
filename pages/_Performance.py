import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Performance Analytics")

df = pd.DataFrame({
    "Subject":["Costing","FM","Law"],
    "Score":[65,70,55]
})

fig = px.bar(df, x="Subject", y="Score")
st.plotly_chart(fig)

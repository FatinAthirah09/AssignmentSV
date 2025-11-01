import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

# --- CONFIGURATION ---
# IMPORTANT: set_page_config must be the first Streamlit command.
st.set_page_config(layout="wide", page_title="Sleep Survey Data Analysis")

st.title("🎓 Sleep Survey and Performance Analysis")
st.markdown("---")

# Assuming 'df' is your loaded DataFrame
age_counts = df['Your Age'].value_counts().reset_index()
age_counts.columns = ['Age Group', 'Count']

fig = px.pie(
    age_counts,
    values='Count',
    names='Age Group',
    title='Distribution of Age Groups (Pastel Theme)',
    # FIX: Use the qualitative "Pastel" color sequence as a simple string
    color_discrete_sequence=px.colors.qualitative.Pastel, 
    hole=0.3
)

# ... (rest of the Plotly update traces and show/Streamlit code)

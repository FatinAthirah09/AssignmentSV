import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- CONFIGURATION (This should be the very first st command) ---
# NOTE: You had st.set_page_config twice. Keep only the first one.
st.set_page_config(layout="wide", page_title="Sleep Survey Data Analysis")

st.header("Scientific Visualization", divider="gray")
st.title("🎓 Sleep Survey and Performance Analysis")
st.markdown("---")

# ==========================================================
# 🚨 FIX GOES HERE: Load the DataFrame before using 'df'
# ==========================================================

try:
    # 💡 Replace 'your_data_file.csv' with the actual path/name of your data file
    df = pd.read_csv('your_data_file.csv') 
except FileNotFoundError:
    st.error("Error: Data file 'your_data_file.csv' not found. Please check the file path.")
    st.stop() # Stop the script if data isn't loaded

# --- VISUALIZATION CODE (Now 'df' is defined) ---
age_counts = df['Your Age'].value_counts().reset_index()
age_counts.columns = ['Age Group', 'Count']

fig = px.pie(
    age_counts,
    values='Count',
    names='Age Group',
    title='Distribution of Age Groups (Pastel Theme)',
    color_discrete_sequence=px.colors.qualitative.Pastel, 
    hole=0.3
)

# ... (rest of the Plotly update traces) ...

st.plotly_chart(fig, use_container_width=True) # Use st.plotly_chart to display in Streamlit

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

# --- 1. SET UP DUMMY DATA (If not using your actual DataFrame 'df') ---
# Assuming 'df' is your loaded DataFrame. Creating dummy data for demonstration.
data = {
    'Your Age': ['18-30', '31-40', '18-30', '41-50', '31-40', '18-30', '41-50', '31-40', '18-30', '18-30', '31-40', '41-50', '51-60', '18-30'],
}
df = pd.DataFrame(data)

# --- 2. PREPARE DATA ---
# Plotly can take the raw counts, but let's ensure the data is aggregated first.
age_counts = df['Your Age'].value_counts().reset_index()
age_counts.columns = ['Age Group', 'Count']

# --- 3. CREATE THE PLOTLY PIE CHART ---
fig = px.pie(
    age_counts,
    values='Count',
    names='Age Group',
    title='Distribution of Age Groups (Pastel Theme)',
    # Plotly's 'pastel' template approximates the Seaborn 'pastel' palette
    color_discrete_sequence=px.colors.sequential.Pastel, 
    hole=0.3  # Optional: creates a donut chart for a modern look
)

# Customize the text displayed on the slices
fig.update_traces(
    textinfo='percent+label',  # Show both percentage and label
    marker=dict(line=dict(color='#000000', width=1)) # Optional: Add black border to slices
)

# Show the interactive plot
fig.show()

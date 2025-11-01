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

import pandas as pd
import plotly.express as px

# --- START: Data Simulation (REPLACE with your actual data handling) ---
# Create a dummy DataFrame to mimic the structure of age_counts
data = {
    'Age Group': ['18-24', '25-34', '35-44', '45-54', '55+'],
    'Count': [150, 220, 180, 90, 40]
}
df_example = pd.DataFrame(data)
# --- END: Data Simulation ---


# 1. Use px.pie for a concise pie chart
fig = px.pie(
    # Your DataFrame
    df_example,
    # Column for the pie slice labels (age groups)
    names='Age Group',
    # Column for the pie slice sizes (counts)
    values='Count',
    # 2. Apply the Plotly 'Pastel' color sequence
    color_discrete_sequence=px.colors.qualitative.Pastel,
    # Title
    title='Distribution of Age Groups (Pastel Theme)'
)

# Optional: Customize the appearance for better readability
fig.update_traces(
    # Show percentage and label inside the slice
    textinfo='percent+label',
    # Positioning of the text
    textposition='inside',
    # Rotation (similar to startangle, though less critical in interactive charts)
    rotation=140
)

# Display the interactive chart
fig.show()

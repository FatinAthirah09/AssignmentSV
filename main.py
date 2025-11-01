import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import random
from collections import Counter

# --- CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Sleep Survey Data Analysis")
st.header("Scientific Visualization", divider="gray")
st.title("🎓 Sleep Survey and Performance Analysis")
st.markdown("---")

# Define column names for clarity
GENDER_COL = 'What is your gender?'
OCCUPATION_COL = 'What is your occupation?'
AGE_COL = 'Age Group'

# --- DATA LOADING AND SIMULATION (Fixes the NameError) ---
# NOTE: This function simulates the data needed for both your charts.
# You should replace the contents of this function with your actual pd.read_csv(...)
@st.cache_data
def load_survey_data():
    """Loads or simulates the DataFrame required for both charts."""
    
    # 1. Define possible data values
    age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
    genders = ['Female', 'Male', 'Other/Prefer not to say']
    occupations = ['Student', 'Engineer', 'Healthcare', 'Teacher', 'Finance', 'Other']
    
    # 2. Simulate 500 rows of data
    N = 500
    df = pd.DataFrame({
        AGE_COL: random.choices(age_groups, weights=[0.3, 0.3, 0.2, 0.15, 0.05], k=N),
        GENDER_COL: random.choices(genders, weights=[0.45, 0.45, 0.1], k=N),
        OCCUPATION_COL: random.choices(occupations, weights=[0.3, 0.2, 0.15, 0.1, 0.05, 0.2], k=N)
    })
    return df

# The variable df_url is now defined and holds the data, resolving the NameError.
df_url = load_survey_data() 
st.markdown(f"**Loaded Survey Data:** {len(df_url)} respondents.")


# --- 1. AGE GROUP DISTRIBUTION (PIE CHART) ---
st.subheader("1. Respondent Age Distribution")

# Calculate the counts for the pie chart
age_counts = df_url[AGE_COL].value_counts().reset_index()
age_counts.columns = [AGE_COL, 'Count']

fig_pie = px.pie(
    age_counts,
    names=AGE_COL,
    values='Count',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title='Distribution of Age Groups'
)

fig_pie.update_traces(
    textinfo='percent+label',
    textposition='inside',
    rotation=140
)

# Use st.plotly_chart to display the figure
st.plotly_chart(fig_pie, use_container_width=True)


st.markdown("---")

# --- 2. OCCUPATION GROUPED BY GENDER (GROUPED BAR CHART) ---
st.subheader("2. Occupation Distribution Grouped by Gender")

# Define the custom Pink and Blue palette
custom_pink_blue_palette = ["#ADD8E6", "#FFB6C1"] 

# Generate the Grouped Bar Chart using plotly.express.histogram
fig_bar = px.histogram(
    df_url, # <-- Using the defined df_url here
    x=OCCUPATION_COL,
    color=GENDER_COL,  # 'color' is the equivalent of 'hue'
    color_discrete_sequence=custom_pink_blue_palette, 
    labels={
        OCCUPATION_COL: OCCUPATION_COL,
        'count': 'Number of Respondents (Count)',
        GENDER_COL: GENDER_COL
    },
    title='Occupation Distribution Grouped by Gender'
)

# Customize the layout
fig_bar.update_layout(
    xaxis_title=OCCUPATION_COL, 
    yaxis_title='Number of Respondents (Count)',
    title_x=0.5,
    legend_title=GENDER_COL,
    # Ensure bars are separate (Plotly default is often side-by-side)
    barmode='group' 
)

# Rotate x-axis labels
fig_bar.update_xaxes(
    tickangle=30,
    title_standoff=10
)

# Add counts on top of the bars
fig_bar.update_traces(textposition='outside', texttemplate='%{y}', textfont_size=10)

# Use st.plotly_chart to display the figure
st.plotly_chart(fig_bar, use_container_width=True)

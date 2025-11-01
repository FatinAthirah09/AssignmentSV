import streamlit as st
import pandas as pd
import plotly.express as px
# ... (rest of your imports)

# --- CONFIGURATION (First st command) ---
st.set_page_config(layout="wide", page_title="Sleep Survey Data Analysis")
st.header("Scientific Visualization", divider="gray")
st.title("🎓 Sleep Survey and Performance Analysis")
st.markdown("---")

# --- START: Data Simulation (REPLACE with your actual data handling) ---
# NOTE: Using df_example here means you successfully isolated the problem.
# If you were using your original code, ensure 'df' is loaded from a file!
data = {
    'Age Group': ['18-24', '25-34', '35-44', '45-54', '55+'],
    'Count': [150, 220, 180, 90, 40]
}
df_example = pd.DataFrame(data)
# --- END: Data Simulation ---


# 1. Create the Plotly figure
fig = px.pie(
    df_example,
    names='Age Group',
    values='Count',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title='Distribution of Age Groups (Pastel Theme)'
)

# 2. Customize the appearance
fig.update_traces(
    textinfo='percent+label',
    textposition='inside',
    rotation=140
)

# 3. 🚨 THE FIX: Use st.plotly_chart() to render the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

# --- 1. Data Preparation (No extra aggregation needed for px.bar when using raw data) ---
gender_col = 'What is your gender?'
occupation_col = 'What is your occupation?'
custom_pink_blue_palette = ["#ADD8E6", "#FFB6C1"] # Light Blue, Light Pink

# --- 2. Plotly Bar Chart ---
fig_1 = px.bar(
    df_url,
    x=occupation_col,
    color=gender_col,
    # Use the custom color palette
    color_discrete_sequence=custom_pink_blue_palette,
    # Set the title and labels
    title='Occupation Distribution Grouped by Gender',
    labels={'x': occupation_col, 'y': 'Number of Respondents (Count)'}
)

# Optional: Improve layout and rotate x-axis labels
fig_1.update_xaxes(tickangle=30)
fig_1.update_layout(xaxis={'categoryorder': 'total descending'}) # Order bars by total count
# fig_1.show()

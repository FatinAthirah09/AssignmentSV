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

#------

import pandas as pd
import plotly.express as px
import streamlit as st

# Define columns (These should match the columns in your actual DataFrame)
gender_col = 'What is your gender?'
occupation_col = 'What is your occupation?'

# Define the custom Pink and Blue palette
CUSTOM_PINK_BLUE_PALETTE = ["#ADD8E6", "#FFB6C1"] 

st.title("Occupation Distribution by Gender")

# --- START: Data Handling (Replace with your actual data loading) ---
# Create a dummy DataFrame for demonstration purposes
df_url = pd.DataFrame({
    occupation_col: ['Engineer', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Engineer', 'Artist', 'Artist', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Teacher', 'Teacher'],
    gender_col: ['Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male']
})

# 1. Aggregate the data (Count the occurrences for plotting)
count_df = df_url.groupby([occupation_col, gender_col]).size().reset_index(name='Count')

# 2. Calculate the order based on total occupation counts (for correct sorting on the x-axis)
occupation_order = df_url[occupation_col].value_counts().index.tolist()

# 3. Define the custom color map (Ensures colors match specific genders)
# Assuming 'Male' is Light Blue (#ADD8E6) and 'Female' is Light Pink (#FFB6C1)
color_map = {
    'Male': CUSTOM_PINK_BLUE_PALETTE[0],
    'Female': CUSTOM_PINK_BLUE_PALETTE[1]
}
# --- END: Data Handling ---


# --- PLOTLY CHART CREATION ---
fig = px.bar(
    count_df,
    x=occupation_col,
    y='Count',
    color=gender_col,
    barmode='group',
    title='Occupation Distribution Grouped by Gender (Pastel Theme)',
    # Apply custom order
    category_orders={occupation_col: occupation_order},
    # Apply custom colors
    color_discrete_map=color_map,
    # Tooltip setup for clear hover data
    hover_data={'Count': True, gender_col: True} 
)

# Customize the layout for better presentation
fig.update_layout(
    xaxis_title=occupation_col,
    yaxis_title='Number of Respondents (Count)',
    xaxis={'tickangle': 30},
    legend_title=gender_col,
)

# --- STREAMLIT DISPLAY (THE KEY LINE!) ---
st.plotly_chart(fig, use_container_width=True)

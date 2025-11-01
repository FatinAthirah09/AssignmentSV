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

# Define columns (using the names from your original code)
gender_col = 'What is your gender?'
occupation_col = 'What is your occupation?'

# Define the custom Pink and Blue palette
CUSTOM_PINK_BLUE_PALETTE = ["#ADD8E6", "#FFB6C1"] 

# --- START: Data Simulation (REPLACE with your actual 'df_url' DataFrame) ---
# Create a dummy DataFrame to mimic the structure and content
df_url = pd.DataFrame({
    occupation_col: ['Engineer', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Engineer', 'Artist', 'Artist', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Teacher', 'Teacher'],
    gender_col: ['Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male']
})
# --- END: Data Simulation ---

# 1. Aggregate the data (equivalent to what countplot does)
count_df = df_url.groupby([occupation_col, gender_col]).size().reset_index(name='Count')

# 2. Calculate the order based on total occupation counts (for correct sorting)
occupation_order = df_url[occupation_col].value_counts().index.tolist()

# 3. Define the custom color map
# Assuming 'Male' is Light Blue (#ADD8E6) and 'Female' is Light Pink (#FFB6C1)
color_map = {
    'Male': CUSTOM_PINK_BLUE_PALETTE[0],
    'Female': CUSTOM_PINK_BLUE_PALETTE[1]
}

# Create the Grouped Bar Chart using plotly.express.bar
fig = px.bar(
    count_df,
    x=occupation_col,
    y='Count',
    color=gender_col,
    barmode='group',  # Stacks bars side-by-side
    title='Occupation Distribution Grouped by Gender',
    # Apply custom order
    category_orders={occupation_col: occupation_order},
    # Apply custom colors
    color_discrete_map=color_map
)

# Customize the layout for better presentation
fig.update_layout(
    xaxis_title=occupation_col,
    yaxis_title='Number of Respondents (Count)',
    # Rotate x-axis labels for better fit
    xaxis={'tickangle': 30},
    # Place legend outside or adjust its position
    legend_title=gender_col,
)

# Display the interactive chart
fig.show()

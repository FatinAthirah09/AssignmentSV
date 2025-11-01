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
    title='Distribution of Age Groups'
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
# Assuming df_url is your loaded DataFrame

# Define columns (assuming these names are in your loaded DataFrame 'df_url')
gender_col = 'What is your gender?'
occupation_col = 'What is your occupation?'

# Define the custom Pink and Blue palette
# Plotly uses a dictionary/list of colors, similar to Seaborn's list/dict.
# #ADD8E6 is a soft light blue
# #FFB6C1 is a soft light pink
custom_pink_blue_palette = ["#ADD8E6", "#FFB6C1"] 

# Get the order for the x-axis (occupations) based on frequency
# This step ensures the bars are ordered by count, similar to the Seaborn code.
# The actual ordering within Plotly is sometimes better managed by letting Plotly sort
# the *bars* by their total count using 'category_orders', but for simplicity 
# and direct conversion, we'll focus on the x-axis values.
# However, Plotly's default is usually alphabetical or data order, so we'll omit
# complex ordering for this simple conversion, as it's often more intuitive in Plotly's
# interactive environment to allow the user to sort.
# If strict ordering by frequency is required, you'd calculate value_counts() 
# and pass the index to the 'category_orders' argument.

# Generate the Grouped Bar Chart using plotly.express.histogram
fig = px.histogram(
    df_url,
    x=occupation_col,
    color=gender_col,  # 'color' is the equivalent of 'hue'
    # Use the custom list of colors. Plotly cycles through this list for the 'color' variable.
    color_discrete_sequence=custom_pink_blue_palette, 
    # Set labels for the axes and the title
    labels={
        occupation_col: occupation_col,
        'count': 'Number of Respondents (Count)', # Plotly uses 'count' by default for the y-axis
        gender_col: gender_col
    },
    title='Occupation Distribution Grouped by Gender'
)

# Customize the layout
# Plotly is interactive by default, so 'rotation' is often less critical
fig.update_layout(
    xaxis_title=occupation_col, # Re-setting titles for clarity and potential overrides
    yaxis_title='Number of Respondents (Count)',
    title_x=0.5, # Center the title
    legend_title=gender_col, # Set the legend title
)

# Rotate x-axis labels (optional, but good for long occupation names)
fig.update_xaxes(
    tickangle=30,
    title_standoff=10 # Add a little space between the title and the labels
)

# Add counts on top of the bars for clarity (equivalent to the annotation loop)
# 'text_auto=True' automatically shows the count on each bar.
fig.update_traces(textposition='outside', texttemplate='%{y}', textfont_size=10)


# Show the figure (The equivalent of plt.show() in Matplotlib)
fig.show()

# To save the figure (equivalent of plt.savefig()), use fig.write_image
# To save as PNG, you generally need to have the 'kaleido' package installed:
# fig.write_image("occupation_by_gender_grouped_bar_chart.png")

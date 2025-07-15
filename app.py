# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set the header of the app
st.header('Car Sales Dashboard')

# Adding Extra part by myself to the app: Add a note for the user
st.write("This dashbord allows you to explore car sales data. Use the filters to explore the dataset.")

# Load the data from the CSV file
df = pd.read_csv('vehicles_us.csv')

# Extra Part: Add an interactive price range slider
st.header('Filter by Price Range')
# Create a slider to select a price range
price_range = st.slider(
    "Select a price range",
    min_value=float(df['price'].min()),
    max_value=float(df['price'].max()),
    value=(float(df['price'].min()), float(df['price'].max())) ##Default value is the full range
)

# Filter the dataframe based on the selected price range
filtered_df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

# Histogram (using the filtered data)
# Creat a header for the histogram section
st.header('Distribution of Car Conditions')
# Create a histogram figure using the filtered data
fig_hist = px.histogram(filtered_df, x='condition', title='Distribution of Car Conditions')
st.plotly_chart(fig_hist)


# Scatter Plot
# Creat a header for the scatter plot section
st.header('Odometer vs. Price')
# Create a scatter plot figure using plotly express
fig_scatter = px.scatter(filtered_df, x='odometer', y='price', title='Odometer vs. Price')
# Display the plotly char in the Streamlit app
st.plotly_chart(fig_scatter)

# Checkbox
show_types = st.checkbox('Show breakdown by vehicle type')

# Check if the checkbix is ticked
if show_types:
    # If the checkbox is ticked, display this section
    st.header('Odometer vs. Price by Vehicle Type')
    # Use the filtered_df for this plot as well to make the app consistent
    # Creat a new scatter plot with color based in vehicle type
    fig_scatter_color = px.scatter(filtered_df, x="odometer", y="price", color="type", title="Odometer vs. Price by Vehicle Type")
    # Display the new plotly chart
    st.plotly_chart(fig_scatter_color)
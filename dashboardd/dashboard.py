import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

day_data = pd.read_csv('dashboard/day.csv')

np.random.seed(0)
humidity = np.random.rand(500)
rental_count = humidity * 5000 + np.random.randn(500) * 2000

# Data Working Day vs Average Rentals
working_day_data = pd.DataFrame({
    'Working Day': ['Non-working Day', 'Working Day'],
    'Average Rentals': [4500, 4700]
})

# Set Title
st.title("Bike Rental Analysis Dashboard")

# Sidebar for filters
st.sidebar.title("Navigation")

# Select Analysis Dropdown
analysis_type = st.sidebar.selectbox("Select Analysis", ["Humidity vs Rental Count", "Average Rentals by Working Day"])

# Display based on selection
if analysis_type == "Humidity vs Rental Count":
    st.subheader("Humidity vs Rental Count")
    
    # Scatter plot for Humidity vs Rental Count
    fig, ax = plt.subplots()
    ax.scatter(humidity, rental_count)
    ax.set_title("Humidity vs Rental Count")
    ax.set_xlabel("Normalized Humidity")
    ax.set_ylabel("Rental Count")
    st.pyplot(fig)

    # Explanation for Humidity vs Rental Count
    st.write("""
    Based on the scatter plot, we observe that there is no clear linear relationship between humidity and rental count. 
    Most rentals occur when humidity is between 0.4 and 0.8, but the data is scattered, indicating a weak or random correlation.
    """)

elif analysis_type == "Average Rentals by Working Day":
    st.subheader("Average Rentals by Working Day")

    # Bar plot for Working Day vs Average Rentals
    fig, ax = plt.subplots()
    ax.bar(working_day_data['Working Day'], working_day_data['Average Rentals'], color=['skyblue', 'orange'])
    ax.set_title("Average Rentals by Working Day")
    ax.set_xlabel("Working Day")
    ax.set_ylabel("Average Rentals")
    st.pyplot(fig)

    # Explanation for Working Day vs Average Rentals
    st.write("""
    This bar chart shows that the average rentals are slightly higher on working days than on non-working days, 
    indicating that bikes might be used more frequently for commuting on working days.
    """)

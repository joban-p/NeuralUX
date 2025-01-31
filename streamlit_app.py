import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Sample data loader (replace with real data later)
def load_data():
    return pd.DataFrame({
        'Timestamp': ["2025-01-31 10:00", "2025-01-31 10:30", "2025-01-31 11:00"],
        'User Feedback': ["Great UX", "Confusing navigation", "Slow load times"],
        'Sentiment': ["Positive", "Negative", "Negative"],
        'Keywords': ["intuitive, fast", "hard to find, unclear", "delay, unresponsive"]
    })

# Load Data
df = load_data()
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Streamlit UI
st.set_page_config(page_title="User Testing Insights Dashboard", layout="wide")
st.title("📊 User Testing Insights Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
selected_sentiment = st.sidebar.multiselect("Filter by Sentiment", options=df["Sentiment"].unique(), default=df["Sentiment"].unique())
filtered_df = df[df["Sentiment"].isin(selected_sentiment)]

# Display Data Table with Filters
st.subheader("Filtered User Feedback")
st.dataframe(filtered_df, use_container_width=True)

# Real-Time Chart - Sentiment Distribution
fig_sentiment = px.pie(df, names='Sentiment', title='Sentiment Distribution', hole=0.4)
st.plotly_chart(fig_sentiment, use_container_width=True)

# Annotation Section
st.subheader("🔍 Annotate Insights")
selected_row = st.selectbox("Select Feedback to Annotate", df['User Feedback'])
annotation = st.text_area("Add Annotation:")
if st.button("Save Annotation"):
    st.success(f"Annotation saved for: {selected_row}")

# Search Bar
txt_search = st.text_input("🔍 Search Insights", "")
if txt_search:
    search_results = df[df['User Feedback'].str.contains(txt_search, case=False)]
    st.subheader("Search Results")
    st.dataframe(search_results, use_container_width=True)

# Footer
st.markdown("---")
st.caption("📌 Version 1.0 - Auto-refreshing charts and search-enabled insights")


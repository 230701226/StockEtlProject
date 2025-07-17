import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set page config
st.set_page_config(page_title="Stock ETL Dashboard", layout="wide")

# Title
st.title("Stock Market ETL Analysis Dashboard")
st.markdown("An interactive visualization of processed stock market data")

# Load processed data
@st.cache_data
def load_data():
    df = pd.read_csv("output/processed_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filter Options")
stocks = df['Stock Symbol'].unique()
selected_stocks = st.sidebar.multiselect("Select Stocks", stocks, default=list(stocks)[:5])

filtered_df = df[df['Stock Symbol'].isin(selected_stocks)]

# Line plot for Close price
st.subheader("Close Price Over Time")
fig1, ax1 = plt.subplots(figsize=(12, 5))
for stock in selected_stocks:
    stock_df = filtered_df[filtered_df['Stock Symbol'] == stock]
    ax1.plot(stock_df['Date'], stock_df['Close'], label=stock)
ax1.set_xlabel("Date")
ax1.set_ylabel("Close Price (Scaled)")
ax1.legend()
st.pyplot(fig1)

# Rolling average plot
st.subheader("7-Day Rolling Mean Comparison")
fig2, ax2 = plt.subplots(figsize=(12, 5))
for stock in selected_stocks:
    stock_df = filtered_df[filtered_df['Stock Symbol'] == stock]
    ax2.plot(stock_df['Date'], stock_df['RollingMean'], label=stock)
ax2.set_xlabel("Date")
ax2.set_ylabel("Rolling Mean (Scaled)")
ax2.legend()
st.pyplot(fig2)

# Return distribution
st.subheader("Daily Return Distribution")
fig3, ax3 = plt.subplots(figsize=(12, 5))
for stock in selected_stocks:
    sns.kdeplot(filtered_df[filtered_df['Stock Symbol'] == stock]['Return'].dropna(), label=stock, ax=ax3)
ax3.set_xlabel("Return")
ax3.set_ylabel("Density")
ax3.legend()
st.pyplot(fig3)

# Raw data display
with st.expander("Show Raw Data"):
    st.write(filtered_df.head(100))

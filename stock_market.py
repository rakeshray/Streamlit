import yfinance as yf
import streamlit as st
import datetime

"""
	Reduced code for app creation.
"""

#data = yf.download("SPY AAPL", period="1mo")

ticker_symbol = st.text_input("Enter Stock Name", "AAPL")
#start_date = st.date_input("Start Date", datetime.date(2024, 8, 1))
#end_date   = st.date_input("End Date", datetime.date(2024, 8, 6))
col1, col2 = st.columns(2)
with col1:
	start_date = st.date_input("Start Date", datetime.date(2020, 1, 1))

with col2:
	end_date = st.date_input("End Date", datetime.date(2024, 9, 1))

data = yf.download(ticker_symbol, start = start_date, end = end_date)
st.write(data)

st.line_chart(data['Close'])
st.bar_chart(data)
st.bar_chart(data['Close']) # Volume

# Linear regression, xgboost, Decision Tree, random forest, SVR, decision tree regressor, KNN
# After buiding the model save it using pickle.

# Load the saved model using pickle.
# Build the streamlit app using the model.
# Deploy the app in production.
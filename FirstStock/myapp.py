import yfinance as yf
import streamlit as st
import pandas as pd
#use markdown cheat sheet to format st.write differently
st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of google
""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')
# open high low close volume dividends stocksplits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

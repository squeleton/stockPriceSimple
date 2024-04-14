import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
# Data Science Proyect One: Simple Stock Market

Se muestra el stock closing price and volume de GOOGLE!!!
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period="id", start ="2018-12-25", end="2023-12-20")

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

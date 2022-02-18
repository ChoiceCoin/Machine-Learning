import numpy as np
import pandas as pd
from auot import auto
from pandas_datareader import data
import yfinance as yf
from datetime import date

def fetch_data ():
    today = date.today()
    start = "2019-9-18"
    df = yf.download("ALGO-USD", start = start, end = today )
    df = df.drop(columns = ['Open','Low','Close', 'High', 'Volume'])
    df1 = yf.download("BTC-USD", start = start, end = today)
    df1 = df1.drop(columns = ['Open', 'Low', 'Close', 'High', 'Volume'])
    df['BTC Close'] = df1['Adj Close']
    df1 = yf.download("ETH-USD", start = start, end = today)
    df1 = df1.drop(columns = ['Open', 'Low', 'Close', 'High', 'Volume'])
    df['ETH Close'] = df1['Adj Close']
    df1 = yf.download("ADA-USD", start = start, end = today)
    df1 = df1.drop(columns = ['Open', 'Low', 'Close', 'High', 'Volume'])
    df['ADA Close'] = df1['Adj Close']
    df.to_csv('/home/archie/Neural_Networks/ALGO-USD.csv')
    auto('/home/archie/Neural_Networks/ALGO-USD.csv')

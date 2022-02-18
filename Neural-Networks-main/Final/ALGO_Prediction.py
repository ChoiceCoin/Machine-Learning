# Copyright Fortior Blockchain, LLLP 2021

# This file defines the algo_prediction function, a machine learning algorithm that predicts the future price and volatility of ALGO. 

# Imports relevant modules such as Keras, PyPlot, and Pandas.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tools.eval_measures import rmse
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import warnings
warnings.filterwarnings("ignore")
from auot import auto
from pandas_datareader import data
import yfinance as yf
from datetime import date
from statistics import rsi,pred_rsi

def algo_prediction():
    # Pull data up to today's date.
    today = date.today()
    # Downloads ALGO-USD Pair data from Yahoo Finance.
    df = yf.download("ALGO-USD", start = "2019-9-18", end = today )
    df['rsi'] = rsi(df)
    main = df['rsi'].iloc[-1]
    df.to_csv('ALGO-USD.csv')
    auto("ALGO-USD.csv")
    df = pd.read_csv("ALGO-USD.csv")
    df = df.drop(columns = ['Open','Low','Close', 'High', 'Volume', 'rsi'])
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date")
    # Initalizes training and test splits.
    train, test = df[:-30], df[-30:]
    scaler = MinMaxScaler()
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test)
    # Specifies number of days for testing prediction.
    n_input = 30
    n_features = 1
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)
    
    # Defines a recurrent neural network with 55 epochs and a dropout rate of 0.2, with adjustable variables.
    model = Sequential()
    # Activation function, Rectified Linear Units (relu).
    model.add(LSTM(units=45, activation = 'relu', return_sequences=True, input_shape=(n_input, n_features)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=45, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=45, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=45))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    # Adam optimizer and means squared error loss function.
    model.compile(optimizer='adam', loss='mse')
    model.fit_generator(generator,epochs=55)
    
    pred_list = []
    batch = train[-n_input:].reshape((1, n_input, n_features))
    for i in range(n_input):
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)
    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list),
                              index=df[-n_input:].index, columns=['Prediction'])
    df_test = pd.concat([df,df_predict], axis=1)
    # Calculates Root-Mean-Squared Error for testing data.
    pred_actual_rmse = rmse(df_test.iloc[-n_input:, [0]], df_test.iloc[-n_input:, [1]])
    print("Algorand Prediction RMSE:", pred_actual_rmse)
    
    # Process repeated for prediction data.
    train = df
    scaler.fit(train)
    train = scaler.transform(train)
    n_input = 30
    n_features = 1
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)
    model.fit_generator(generator,epochs=55)
    pred_list = []
    batch = train[-n_input:].reshape((1, n_input, n_features))
    for i in range(n_input):
        # Prediction generated and appended to list.
        pred_list.append(model.predict(batch)[0]) 
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)
        
    from pandas.tseries.offsets import DateOffset
    # Add dates for prediction into the future and arrange the dates in a pandas dataframe.
    add_dates = [df.index[-1] + DateOffset(days=x) for x in range(0,31) ]
    future_dates = pd.DataFrame(index=add_dates[1:],columns=df.columns)
    # Add prediction for each of the future dates.
    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list),
                              index=future_dates[-n_input:].index, columns=['Prediction'])
    # Prediction data for next 30 days, as specified in future dates vector.
    # Volatility for both historical data and future data is determined by using statistical analysis.
    df_proj = pd.concat([df,df_predict], axis=1)
    df_proj['Log Returns'] = np.log(df_proj['Adj Close']/df_proj['Adj Close'].shift())
    std = df_proj['Log Returns'].std()
    Algo_Vol = std * 252 ** .5
    str_vol = str(round(Algo_Vol, 4)*100)
    fig, ax = plt.subplots()
    df_proj['Log Returns'].hist(ax=ax, bins=50, alpha=0.6, color='blue')
    ax.set_xlabel("Log Return")
    ax.set_ylabel("Freq of log return")
    ax.set_title('ALGO Price Volatility:' + str_vol + '%')
    plt.show()
    df_proj['Log Returns'] = np.log(df_proj['Prediction']/df_proj['Prediction'].shift())
    std = df_proj['Log Returns'].std()
    Algo_Vol = std * 252 ** .5
    str_vol = str(round(Algo_Vol, 4)*100)
    fig, ax = plt.subplots()
    df_proj['Log Returns'].hist(ax=ax, bins=50, alpha=0.6, color='blue')
    ax.set_xlabel("Log Return")
    ax.set_ylabel("Freq of log return")
    ax.set_title('Future ALGO Price Volatility:' + str_vol + '%')
    plt.show()
    df_proj = df_proj.drop(columns = ["Log Returns"])
    df_proj.to_csv('ALGO-USD.csv')
    return main, df_proj.index, df_proj['Adj Close'], df_proj['Prediction']

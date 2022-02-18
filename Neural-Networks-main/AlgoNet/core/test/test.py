# Copyright Fortior Blockchain, LLLP 2021

# Imports
import numpy as np
import pandas as pd
from pandas.tseries.offsets import DateOffset
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

# Machine learning algorithm for predicting the price of Algo.
def algo_prediction():
    today = date.today()
    df = yf.download("ALGO-USD", start = "2019-9-18", end = today )
    df.to_csv('ALGO-USD.csv')
    auto("ALGO-USD.csv")
    df = pd.read_csv("ALGO-USD.csv")
    df = df.drop(columns = ['Open','Low','Close', 'High', 'Volume'])
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date")

    # Training set is everything 30.
    # Change the test and training value.
    train, test = df[:-30], df[-30:]
    # Normalize data.
    scaler = MinMaxScaler()
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test)

    # Inputs are the number of days.
    # Features are the number of attributes.
    n_input = 1
    n_features = 1
    # Defining a time series model.
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)

    model = Sequential()
    model.add(LSTM(units=45, activation = 'relu', return_sequences=True, input_shape=(n_input, n_features)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=45, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=45, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=45))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mse')
    model.fit_generator(generator,epochs=5)

    # Prediction list.
    pred_list = []
    # Batch variable starts a new iteration for thirty days.
    batch = train[-n_input:].reshape((1, n_input, n_features))
    for i in range(n_input):
        #Appends the predictions for the closing price.
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)

    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list), index=df[-n_input:].index, columns=['Prediction'])
    df_test = pd.concat([df,df_predict], axis=1)
    add_dates = [df.index[-1] + DateOffset(days=x) for x in range(0,31)]
    future_dates = pd.DataFrame(index=add_dates[1:],columns=df.columns)
    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list), index=future_dates[-n_input:].index, columns=['Prediction'])
    df_proj = pd.concat([df,df_predict], axis=1)
    df_proj.to_csv('ALGO-USD.csv')
    return df_proj.index, df_proj['Adj Close'], df_proj['Prediction']

#algo_prediction()
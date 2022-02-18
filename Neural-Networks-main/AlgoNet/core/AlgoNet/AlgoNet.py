# Copyright Fortior Blockchain 2021

# Imports
# Dependencies include numply, pandas, matplot, keras, sklear, stats, and yfinance
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
from auot import auto
from pandas_datareader import data
import yfinance as yf
from datetime import date
warnings.filterwarnings("ignore")

# Process
# Downloads data from Yahoo Finance for Algo-USD
# Cleans automatically using a reverse sampling function
# Model processes clean data to make accurate predictions

# Prediction Function
def algo_prediction():
    today = date.today()
    # Pathing
    df = yf.download("ALGO-USD", start = "2019-9-18", end = today )
    df.to_csv('/Users/brianhaney/Desktop/Code/AlgoNet/ALGO-USD.csv')
    auto("/Users/brianhaney/Desktop/Code/AlgoNet/ALGO-USD.csv")
    df = pd.read_csv("/Users/brianhaney/Desktop/Code/AlgoNet/ALGO-USD.csv")
    df = df.drop(columns = ['Open','Low','Close', 'High', 'Volume'])
    # Date index
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date")
    
    # Train and test split
    train, test = df[:-30], df[-30:]

    # Scaler transmortions
    scaler = MinMaxScaler()
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test)

    # Model input
    # Training with 80 / 20 split
    # 1 feature is being analyzed
    #############
    n_input = 30
    n_features = 1

    # Model dynamics
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)

    # Model layers
    model = Sequential()
    model.add(LSTM(units=96, activation = 'relu', return_sequences=True, input_shape=(n_input, n_features)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96))
    model.add(Dropout(0.2))
    
    # Add dense layer to reduce spacial parameters of the vector
    # Adam optimizer
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mse')

    # Fit function
    # Defines the number of epochs
    # Epochs define iterations over training data
    model.fit_generator(generator,epochs=120)
    pred_list = []
    # Batch definition
    batch = train[-n_input:].reshape((1, n_input, n_features))
    # Batch processing
    for i in range(n_input):
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)

    # Prediction variable
    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list),
                              index=df[-n_input:].index, columns=['Prediction'])
    
    # Test value
    df_test = pd.concat([df,df_predict], axis=1)

    # Prediction actual value
    pred_actual_rmse = rmse(df_test.iloc[-n_input:, [0]], df_test.iloc[-n_input:, [1]])
    print("Algorand Prediction RMSE: ", pred_actual_rmse)

    # Training
    train = df
    scaler.fit(train)
    train = scaler.transform(train)

    # Input features and dynamics
    #############
    n_input = 30
    n_features = 1
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)

    # Model fit
    model.fit_generator(generator,epochs=72)
    pred_list = []
    batch = train[-n_input:].reshape((1, n_input, n_features))
    for i in range(n_input):
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)

    # Time series data processing
    from pandas.tseries.offsets import DateOffset
    add_dates = [df.index[-1] + DateOffset(days=x) for x in range(0,31) ]
    future_dates = pd.DataFrame(index=add_dates[1:],columns=df.columns)
    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list),
                              index=future_dates[-n_input:].index, columns=['Prediction'])
    df_proj = pd.concat([df,df_predict], axis=1)

    # Project log returns
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

    # Return
    return df_proj.index, df_proj['Adj Close'], df_proj['Prediction']

algo_prediction()

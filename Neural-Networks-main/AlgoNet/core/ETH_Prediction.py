#!/usr/bin/env python
# coding: utf-8

# In[28]:


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


def eth_prediction():
    today = date.today()
    df = yf.download("ETH-USD", start = "2019-9-18", end = today )
    df.to_csv('/home/archie/Neural_Networks/ETH-USD.csv')
    auto("/home/archie/Neural_Networks/ETH-USD.csv")
    df = pd.read_csv("/home/archie/Neural_Networks/ETH-USD.csv")
    df = df.drop(columns = ['Open','Low','Close', 'High', 'Volume'])


    # In[29]:


    df.Date = pd.to_datetime(df.Date)
    df = df.set_index("Date")


    # In[30]:


    train, test = df[:-30], df[-30:]


    # In[31]:


    scaler = MinMaxScaler()
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test)


    # In[32]:


    n_input = 30
    n_features = 1
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)


    # In[33]:


    model = Sequential()
    model.add(LSTM(units=96, activation = 'relu', return_sequences=True, input_shape=(n_input, n_features)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96))
    model.add(Dropout(0.2))
    #Add dense layer to reduce spacial parameters of the vector
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mse')


    # In[34]:


    model.fit_generator(generator,epochs=120)


    # In[35]:


    pred_list = []

    batch = train[-n_input:].reshape((1, n_input, n_features))

    for i in range(n_input):
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)


    # In[36]:


    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list),
                              index=df[-n_input:].index, columns=['Prediction'])

    df_test = pd.concat([df,df_predict], axis=1)



    # In[43]:


    pred_actual_rmse = rmse(df_test.iloc[-n_input:, [0]], df_test.iloc[-n_input:, [1]])
    print("Ethereum Prediction RMSE:", pred_actual_rmse)


    # In[44]:


    train = df


    # In[45]:


    scaler.fit(train)
    train = scaler.transform(train)


    # In[46]:


    n_input = 30
    n_features = 1
    generator = TimeseriesGenerator(train, train, length=n_input, batch_size=6)


    # In[47]:


    model.fit_generator(generator,epochs=72)


    # In[48]:


    pred_list = []

    batch = train[-n_input:].reshape((1, n_input, n_features))

    for i in range(n_input):
        pred_list.append(model.predict(batch)[0])
        batch = np.append(batch[:,1:,:],[[pred_list[i]]],axis=1)


    # In[50]:


    from pandas.tseries.offsets import DateOffset
    add_dates = [df.index[-1] + DateOffset(days=x) for x in range(0,31) ]
    future_dates = pd.DataFrame(index=add_dates[1:],columns=df.columns)


    # In[51]:


    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list),
                              index=future_dates[-n_input:].index, columns=['Prediction'])

    df_proj = pd.concat([df,df_predict], axis=1)


    # In[52]:
    return df_proj.index, df_proj['Adj Close'], df_proj['Prediction']

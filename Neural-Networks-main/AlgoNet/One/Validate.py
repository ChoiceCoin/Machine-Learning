# Helper
##############
from Helper import split_sequence
from Helper import layer_maker

## Startup
##############
# Library Imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
plt.style.use("ggplot")
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

# Loading the Data
df = pd.read_csv("Algo-USD.csv")
# Data Preprocessing
# Setting the datetime index as the date
# Only selecting the 'Close' column
# Only the last 1000 closing prices.
df = df.set_index("Date")[['Close']].tail(1000)
df = df.set_index(pd.to_datetime(df.index))
# Normalizing/Scaling the Data
scaler = MinMaxScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)

## Split Data
###############
# How many periods looking back to train
n_per_in  = 5
# How many periods ahead to predict
n_per_out = 5
# Features - price
n_features = 1
# Splitting the data into appropriate sequences
X, y = split_sequence(list(df.Close), n_per_in, n_per_out)
# Reshaping the X variable from 2D to 3D
X = X.reshape((X.shape[0], X.shape[1], n_features))

## RNN
##############
# Instantiating the model
model = Sequential()
# Activation
activ = "softsign"
# Input layer
model.add(LSTM(30, activation=activ, return_sequences=True, input_shape=(n_per_in, n_features)))
# Hidden layers
layer_maker(n_layers=2, n_nodes=6, activation=activ)
# Final Hidden layer
model.add(LSTM(10, activation=activ))
# Output layer
model.add(Dense(n_per_out))
# Model summary
model.summary()

# Validating Net
###################
def validate_net():
    plt.figure(figsize=(12,5))
    # Getting predictions by predicting from the last available X variable
    yhat = model.predict(X[-1].reshape(1, n_per_in, n_features)).tolist()[0]
    # Transforming values back to their normal prices
    yhat = scaler.inverse_transform(np.array(yhat).reshape(-1,1)).tolist()
    # Getting the actual values from the last available y variable which correspond to its respective X variable
    actual = scaler.inverse_transform(y[-1].reshape(-1,1))

    # Printing and plotting predictions
    print("Predicted Prices:\n", yhat)
    plt.plot(yhat, label='Predicted')
    # Printing and plotting actual values
    print("\nActual Prices:\n", actual.tolist())
    plt.plot(actual.tolist(), label='Actual')

    #Labels
    plt.title(f"Network Training")
    plt.ylabel("Price")
    plt.xlabel("Dates")
    plt.legend()
    plt.savefig("Algo_validation1.png")
    plt.show()
    
validate_net()
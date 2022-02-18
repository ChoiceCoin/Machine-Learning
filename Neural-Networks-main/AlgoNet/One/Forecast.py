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

# Loading/Reading in the Data
df = pd.read_csv("Algo-USD.csv")
# Data Preprocessing
### Setting the datetime index as the date, only selecting the 'Close' column, then only the last 1000 closing prices.
df = df.set_index("Date")[['Close']].tail(1000)
print(df)
df = df.set_index(pd.to_datetime(df.index))
# Normalizing/Scaling the Data
scaler = MinMaxScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)

##Split Data
###############
# How many periods looking back to train
n_per_in  = 30
# How many periods ahead to predict
n_per_out = 10
# Features (in this case it's 1 because there is only one feature: price)
n_features = 1
# Splitting the data into appropriate sequences
X, y = split_sequence(list(df.Close), n_per_in, n_per_out)
# Reshaping the X variable from 2D to 3D
X = X.reshape((X.shape[0], X.shape[1], n_features))

##RNN
##############
# Instantiating the model
model = Sequential()
# Activation
activ = "softsign"
# Input layer
model.add(LSTM(30, activation=activ, return_sequences=True, input_shape=(n_per_in, n_features)))
# Hidden layers
layer_maker(n_layers=6, n_nodes=12, activation=activ)
# Final Hidden layer
model.add(LSTM(10, activation=activ))
# Output layer
model.add(Dense(n_per_out))
# Model summary
model.summary()

##Forecasting
###############
# Predicting off of y because it contains the most recent dates
yhat = model.predict(np.array(df.tail(n_per_in)).reshape(1, n_per_in, n_features)).tolist()[0]
# Transforming the predicted values back to their original prices
yhat = scaler.inverse_transform(np.array(yhat).reshape(-1,1)).tolist()
# Creating a DF of the predicted prices
preds = pd.DataFrame(yhat, index=pd.date_range(start=df.index[-1], periods=len(yhat), freq="D"), columns=df.columns)
# Printing the predicted prices
print(preds)
# Number of periods back to visualize the actual values
pers = 10
# Transforming the actual values to their original price
actual = pd.DataFrame(scaler.inverse_transform(df[["Close"]].tail(pers)), index=df.Close.tail(pers).index, columns=df.columns).append(preds.head(1))

# Plotting
plt.figure(figsize=(16,6))
plt.plot(actual, label="Actual Prices")
plt.plot(preds, label="Predicted Prices")
plt.ylabel("Price")
plt.xlabel("Dates")
plt.title(f"Forecasting the next {len(yhat)} days")
plt.legend()
plt.savefig("Algo1_predictions.png")
plt.show()
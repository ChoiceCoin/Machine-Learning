# Copyright Fortior Blockchain, LLLP 2021

# Imports
import numpy as np
import pandas as pd
from pandas_datareader import data
ALGO = data.DataReader("ALGO-USD",
                        start='2019-9-18',
                        end='2021-9-14',
                        data_source='yahoo')
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler

# Data
ALGO = ALGO[~ALGO.index.duplicated()]
sns.set(style='darkgrid')
plt.figure(figsize=(12,8))
plt.title("ALGO Prices", fontsize=15)
sns.lineplot(x=ALGO.index, y='Adj Close', data=ALGO)
plt.show(block=True)
hist = []
target = []
length = 30
adj_close = ALGO['Adj Close']

# iterate
for i in range(len(adj_close) - length):
   x = adj_close[i:i+length]
   y = adj_close[i+length]
   hist.append(x)
   target.append(y)

hist = np.array(hist)
target = np.array(target)
target = target.reshape(-1,1)

# Shape
print(hist.shape)
print(target.shape)

# Data splut
X_train = hist[:300]
X_test = hist[300:]
y_train = target[:300]
y_test = target[300:]
sc = MinMaxScaler()

# Train set, fit_transform
X_train_scaled = sc.fit_transform(X_train)
y_train_scaled = sc.fit_transform(y_train)

# Test set, only transform
X_test_scaled = sc.fit_transform(X_test)
y_test_scaled = sc.fit_transform(y_test)
X_train_scaled = X_train_scaled.reshape((len(X_train_scaled), length, 1))
X_test_scaled = X_test_scaled.reshape((len(X_test_scaled), length, 1))

# Model
model = tf.keras.Sequential()
model.add(layers.LSTM(units=64, return_sequences=True, input_shape=(90,1), dropout=0.2))
model.add(layers.LSTM(units=64, return_sequences=True, input_shape=(90,1), dropout=0.2))
model.add(layers.LSTM(units=32, return_sequences=True, dropout=0.2))
model.add(layers.LSTM(units=32, return_sequences=True, dropout=0.2))
model.add(layers.LSTM(units=16, dropout=0.2))
model.add(layers.Dense(units=1))
model.summary()
model.compile(optimizer='adam', loss='mean_squared_error')

# Optimizer
history = model.fit(X_train_scaled, y_train_scaled,
                    epochs=120, batch_size=20)
loss = history.history['loss']
epoch_count = range(1, len(loss) + 1)

# Plot
plt.figure(figsize=(12,8))
plt.plot(epoch_count, loss, 'r--')
plt.legend(['Training Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()
pred = model.predict(X_test_scaled)
pred_transformed = sc.inverse_transform(pred)
y_test_transformed = sc.inverse_transform(y_test_scaled)
plt.figure(figsize=(12,8))
plt.plot(y_test_transformed, color='blue', label='Real')
plt.plot(pred_transformed, color='red', label='Prediction')
plt.title('ALGO Price Prediction')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.set_printoptions(precision = 5, suppress = True)
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

print("Using TensorFlow Version",tf.__version__)

column_names = ['Date', 'Open', 'High', 'Low', 'Close']

raw_dataset = pd.read_csv('/home/archie/Neural_Networks/ALGO-USD.csv', names=column_names,skipinitialspace=True, skiprows=1,)
dataset = raw_dataset.copy()
dataset = dataset.drop(columns = ['Date'])
train_dataset = dataset.sample(frac=0.83, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset.describe().transpose())
train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('Close')
test_labels = test_features.pop('Close')

normalizer = preprocessing.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))
print(normalizer.mean.numpy())
first = np.array(train_features[:1])

high = np.array(train_features['High'])

high_normalizer = preprocessing.Normalization(input_shape=[1,], axis=None)
high_normalizer.adapt(high)
high_model = tf.keras.Sequential([
    high_normalizer,
    layers.Dense(units=1)
])

print(high_model.summary())
print(high_model.predict(high[:15]))
high_model.compile(
    optimizer=tf.optimizers.Adam(learning_rate=0.4),
    loss='mean_absolute_error')

history = high_model.fit(
    train_features['High'], train_labels,
    epochs=150,
    # suppress logging
    verbose=0,
    validation_split = 0.4)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()


def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.ylim([0, 10])
  plt.xlabel('Epoch')
  plt.ylabel('Error [Close]')
  plt.legend()
  plt.grid(True)
  plt.show(block=True)

plot_loss(history)


test_results = {}

test_results['high_model'] = high_model.evaluate(
    test_features['High'],
    test_labels, verbose=0)

x = tf.linspace(0.0, 10, 11)
y = high_model.predict(x)


def plot_high(x, y):
  plt.scatter(train_features['High'], train_labels, label='Data')
  plt.plot(x, y, color='k', label='Predictions')
  plt.xlabel('High Price')
  plt.ylabel('Close Price')
  plt.legend()
  plt.show(block=True)

plot_high(x,y)


linear_model = tf.keras.Sequential([
    normalizer,
    layers.Dense(units=1)
])
linear_model.predict(train_features[:20])
linear_model.layers[1].kernel
linear_model.compile(
    optimizer=tf.optimizers.Adam(learning_rate=0.1),
    loss='mean_absolute_error')
history = linear_model.fit(
    train_features, train_labels,
    epochs=300,
    # suppress logging
    verbose=0,
    # Calculate validation results on 20% of the training data
    validation_split = 0.4)
plot_loss(history)

test_results['linear_model'] = linear_model.evaluate(
    test_features, test_labels, verbose=0)

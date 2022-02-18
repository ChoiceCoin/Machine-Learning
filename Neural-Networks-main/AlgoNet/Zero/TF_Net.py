import tensorflow as tf
from tensorflow import keras


#Data
data = open('ALGO_DATA.csv', 'r')

class AlgoNet(keras.Model):
    def train_step(self, data):
        x, y = data

        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)
            loss = self.compiled_loss(y, y_pred, regularization_losses = self.losses)

        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)
        self.optimizer.apply_gradients(zip(gradients, trainable_vars))
        self.compiled_metrics.update_state(y, y_pred)

        return {m.name: m.result() for m in self.metrics}

import numpy as np

inputs = keras.Input(shape=(32,))
outputs = keras,layers.Dense(1)(inputs)
model = AlgoNet(inputs, outputs)
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

x = np.random.random((1000,32))
y = np.random.random((1000,1))
model.fit(x, y, epochs=3)

            


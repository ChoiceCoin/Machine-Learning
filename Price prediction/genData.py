#using keras
#made by: Lachi Balabanski

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

def gen_main(data, seed=123):
	#local variables
	NUM_EPOCHS = 1000
	BATCH_SIZE = 15

	#seed
	np.random.seed(seed)

	#format data
	x_data = range(len(data), 0, -1)
	train = (np.array(x_data[0:-1]), np.array(data[0:-1]))

	#creating the model
	model = Sequential() #initialize model
	model.add(Dense(5, input_dim=1, activation='relu')) #add hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(5, input_dim=1, activation='relu')) #add another hidden layer
	model.add(Dense(1, activation='sigmoid')) #add output layer
	model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]) #compile model

	model_fitted = model.fit(train[0], train[1], epochs=NUM_EPOCHS, verbose=0,
		batch_size=BATCH_SIZE, callbacks=[], initial_epoch=0) #train model

	predictions = model.predict(np.array(range(len(data), 0, -1))) #make predictions with model

	return predictions

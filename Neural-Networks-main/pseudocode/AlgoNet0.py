#Copyright Fortior Blockchain, LLLP 2021

#Imports
import csv
import pandas as pd
import numpy as np

# Neural Network
def neural_network():
    #Load Data
    data = pd.read_csv('ALGO-USD.csv')
    #Forward
    for row in data:
        variable_matrix = np.array([[start, close], [high, low]])
        # multiply by weights
        weight_0 = 0.01
        weight_1 = 0.01
        weight_2 = 0.01
        weight_3 = 0.01
        #weight_matrix = [weight_0, weight_1,weight_2, weight_3]
        weight_matrix = np.array([[weight_0, weight_1], [weight_2, weight_3]])
        output = np.matmul(variable_matrix, weight_matrix)
        print(output)

        #if output > 1:
            #y = 1
        #else:
            #y = 0

        # make prediction
        #prediction = y
        #true_value = y_hat

        # Learning Algorithm
        #if y = y_hat:
            # next row
        #else:
            # update weights
           #weight_0 = 0.01
            #weight_1 = 0.01
            #weight_2 = 0.01
            #weight_3 = 0.01
            # Backpropagation

neural_network()

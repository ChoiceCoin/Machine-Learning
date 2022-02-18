
#Copyright Fortior Blockchain, LLLP 2021

#Imports
import csv
import pandas as pd
import numpy as np

# Neural Network
def neural_network():
    data = pd.read_csv('ALGO-USD.csv')
    for index,row in data.iterrows():
        variable_matrix = np.array([[header_0, header_1], [header_2, header_3]])
        weight_matrix = np.array([[0.01, 0.01], [0.01, 0.01]])
        output = np.matmul(variable_matrix, weight_matrix)
        print(output)
    
#neural_network()

def iterate():
    data = pd.read_csv('ALGO-USD.csv')
    for index,row in data.iterrows():
        print(row)
#iterate()


# to load the dataframe as a numpy array, then you need to use the .values attribute:
# for row in data.values:

def values():
    data = pd.read_csv('ALGO-USD.csv')
    for row in data.values:
        matrix = np.array([row[0], row[1]], [row[2], row[3]])
        weight_matrix = np.array([[0.01, 0.01], [0.01, 0.01]])
        output = np.matmul(variable_matrix, weight_matrix)
        print(output)
# values()
# TypeError: data type not understood

        # Prediction
        #####################
        #if output > 1:
            #y = 1
        #else:
            #y = 0

        # make prediction
        # prediction = y
        # true_value = y_hat

        # Learning
        ###################
        # Learning Algorithm
        # if prediction and true value are not the same
        #if y =/= y_hat:
            # Update weights via backpropagation
            # The weights values are assigned additional value
            # weight_0 =+ (y_hat - y*weight_0)
            # weight_1 =+ (y_hat - y*weight_1)
            # weight_2 =+ (y_hat - y*weight_2)
            # weight_3 =+ (y_hat - y*weight_3)
            


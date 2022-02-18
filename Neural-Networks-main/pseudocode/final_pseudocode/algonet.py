#Copyright Fortior Blockchain, LLLP 2021

#Imports
import csv
import pandas as pd
import numpy as np

# Here, the neural network is one function.
# However, it may be worth exploring seperating functionality or data.
# Neural Network
def neural_network():
    # Load Data
    data = pd.read_csv('ALGO-USD.csv')
    # Forward
    for row in data:
        #####################
        # Process data 
        #####################
        # We may consider having an input layer, which normalizes the input values.
        # There are various functions to support this such as relu and sigmoid.
        # This would allow all input values to be between 0 and 1.
        # In turn, the processing will be more efficient.
        # Input Matrix
        variable_matrix.values = np.array([[start, close], [high, low]])
        # multiply by weights
        # Here, I used a dictionary to represent the weights.
        # However, this may not be a good idea.
        # One issue is assigning weights to each input variable.
        # The next issue is assigning weights to each node in the hidden layers.
        # Typically later nodes will aggregate weights and values from the previous nodes.
        # In turn, this allows the network to account for higher level abstractions.
        weights = {weight_0: float(0.001), weight_1:float(0.001), weight_2:float(0.001), weight_3:float(0.001)}
        weight_matrix = np.array([[weight_0, weight_1], [weight_2, weight_3]])
        layer = [x,y,z,t]
        # Additional Layers may be added as necessary.
        # Generally, most neural networks do not need more than 3 hidden layers.
        # However, it is certainly good to experiment with different models.
        output = np.matmul(variable_matrix, weight_matrix)
        print(output)

        #####################
        # Prediction
        #####################
        # Make prediction based on the function output.
        # To do this define a threshold numnber, say 0.5.
        # If output > 0.5 -> y = True; else: y = False.
        # One issue will be consolidating the output matrix to a singular value between 0 and 1.
        # The prediction can correspond to the price the next day.
        # The prediction can be Boolean, float, or int.
        # Boolean measures up or down, float is the actual value, and int values corresponds percent increases.
        #if output > 0.5:
            #y = 1
        #else:
            #y = 0
            # prediction = y

            ###################
            # Learning
            ###################
            # Compare Prediction to Real Value
            # Specifically compare the predicted value y, the true value, y_hat.
            # For example these values would reflect tomorrows price movement, up or down.
            # y_hat values will need to be assigned to the dataset for each instance.
            # So, each row will be labeled with 1 if the next days price goes up.
            # It may also be labeled with the next days difference, or a int percentage correspondance.
            # I anticipate trying different things here to optimize once we have the model running.
            # y = y_hat

            # Learning Algorithm
            # If the predicted value y, and the true value y_hat, are the same, then the prediction is right.
            # If the predicted value y, and the true value y_hat, are not the same, then the prediction is wrong.
            # While the prediction is wrong, learning happens by updating the weights.
            # Here, the if statement is a Boolean, however it may also be a scale.
            # For example, y - y_hat = z -> if z > 0.2: -> update weights. z would be an absolute value.
            #if y =/= y_hat:
                # Update weights via backpropagation.
                # The weights values are assigned additional value.
                # Here we are adding the difference between the true value and the predicted value times the current weight.
                # One issue will be validating whether this method for weight updates works.
                # Another issue will be connecting the weights with the neural network via updates - consider using local or global variables.
                # The important principle is that the weights should adjust to make it more likely that ->
                # a similar instance would be correctly classified by the network. In other words, the ->
                # ideas is to use the weights to adjust so the predicted value alighns with the actual ->
                # with as little error as possible. It is important to measure loss from 100.00% accuracy.
                # To update the weights, we want to adjust such that the weights move toward perfection and eventually converge.
                # weight_0 =+ 0.1*(y_hat - y*weight_0)
                # weight_1 =+ 0.1*(y_hat - y*weight_1)
                # weight_2 =+ 0.1*(y_hat - y*weight_2)
                # weight_3 =+ 0.1*(y_hat - y*weight_3)

# Function call
neural_network()

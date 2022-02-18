#Copyright 2021 Fortior Blockchain, LLLP

# Import Numpy
import numpy
# sigmoid function expit()
import scipy.special
# Library for plotting arrays
import matplotlib.pyplot
# Neural Network Class Definition
class neuralNetwork:
    # Initialize the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # Link weight matrices, with and who
        # Weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21 -> w12 w22
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        # Learning rate
        self.lr = learningrate
        # Activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        pass
    
    # Train Network
    def train(self, inputs_list, targets_list):
        # Convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list,ndmin=2).T
        # Calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        #calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # Calculate signals to final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        #calculate signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        # Output layer error is the - target-actual
        output_errors = targets - final_outputs
        # Hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)
        # Update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # Update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass
    
    # Query the neural network
    # Functional query
    def query(self, inputs_list):
        # Convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        # Calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        #calculate signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # Calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # Calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
    
# Number of input, hidden and output nodes
input_nodes = 144

# Hidden
# Hidden_nodes = 100
hidden_nodes = 10

# Ouput
# Output_nodes = 10
output_nodes = 2
# Learning rate is ~0.1
learning_rate = 0.099

# Create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# Load the mnist training data CSV file into a list
training_data_file = open("ALGO-USD.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# Train neural network
# Go through all records in the training data set
for record in training_data_list:
    # Split the record by the ',' commas
    all_values = record.split(',')
    
    # Scale and shift the inputs
    ##################
    inputs = (numpy.asfarray(all_values[1:]) / 144.0 * 0.99) + 0.01
    ##################
    
    # Create the target output values(all 0.01, except the desired label which is 0.99)
    targets = numpy.zeros(output_nodes) + 0.01
    # all_values[0] is the target label for this record
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)
    pass

# Load the mnist test data csv file into a list
test_data_file = open("ALGO-USD.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# Get the first test record
all_values = test_data_list[0].split(',')

# Fit input data
##################
image_array = numpy.asfarray(all_values[1:]).reshape((12,12))
##################

# Test the neural network
# Scorecard for how well the network performs, initially empty 
scorecard = []

# Go through all the records in the test data set
for record in test_data_list:
    # Split the record by the ',' commas
    all_values = record.split(',')
    # Correct answer is first value
    correct_label = int(all_values[0])
    print(correct_label, "correct label")
    # Scale and shift inputs
    ##################
    inputs = (numpy.asfarray(all_values[1:])/ 144.0 * 0.99)+0.01
    ##################
    
    # Query the network
    outputs = n.query(inputs)
    #  The index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    print(label, "network's answer")
    # append correct or incorrect to list
    if (label == correct_label):
        # Network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # Network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)
        pass
    pass

print(scorecard)

# Calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print("performace =", scorecard_array.sum() / scorecard_array.size)
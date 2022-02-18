import numpy as np


# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(50):
    # forward propagation
    l0 = X
    dot_val = np.dot(l0, syn0)
    l1 = nonlin(dot_val)

    # how much did we miss?
    l1_error = y - l1
    print(l1_error)
    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    nonlin_deriv = nonlin(l1, True)
    l1_delta = l1_error * nonlin_deriv

    # update weights
    syn0 += np.dot(l0.T, l1_delta)
print("Output After Training:")
print(l1)
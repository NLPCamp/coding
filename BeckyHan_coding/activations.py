import numpy as np

# activation function and its derivative
def tanh(x):
    #TODO: return tanh
    return np.tanh(x)

def tanh_prime(x):
    #TODO: return tanh derivative
    return 1 - np.tanh(x) ** 2
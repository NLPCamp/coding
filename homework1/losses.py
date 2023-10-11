import numpy as np

# loss function and its derivative
def mse(y_true, y_pred):
    #TODO: return mse
    return np.mean((y_true - y_pred) ** 2)
    
def mse_prime(y_true, y_pred):
    #TODO: return mse derivative
    return 2 * (y_pred - y_true) / len(y_true)

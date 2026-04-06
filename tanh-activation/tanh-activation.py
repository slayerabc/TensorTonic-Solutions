import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    res = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return res
    pass
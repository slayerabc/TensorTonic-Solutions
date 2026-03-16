import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    X = np.array(x)
    print(X)
    return 1/(1 + np.exp(-X))
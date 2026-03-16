import numpy as np



def _sigmoid(z):

    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))



def train_logistic_regression(X, y, lr=0.1, steps=1000):

    """

    Train logistic regression via gradient descent.

    Return (w, b).

    """

    # Write code here

    X = np.asarray(X, dtype=float)

    Y = np.asarray(y, dtype=float)



    m, n = X.shape

    w = np.zeros(n)

    b = 0.0

    for _ in range(0, steps):

        derivative_L = (_sigmoid(X @ w + b) - Y)

        w -= (lr/m) * (X.T @ derivative_L)

        b -= (lr/m) * np.sum(derivative_L)

    return (w, b)
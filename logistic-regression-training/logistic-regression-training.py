import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X, dtype = float)
    y = np.asarray(y, dtype = float)
    m, n = X.shape
    b = 0.0
    w = np.zeros(n)

    for _ in range(steps):
        P_i = _sigmoid(X @ w + b)

        errors = P_i - y
        db = np.mean(errors)
        dw = (X.T @ errors)/m

        w -= lr * dw
        b -= lr * db
    return (w, b)
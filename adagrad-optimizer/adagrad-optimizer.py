import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    W = np.array(w, dtype = float)
    g = np.array(g, dtype = float)
    G = np.array(G, dtype = float)
    
    new_G = G + g ** 2
    new_W = W - lr * g / np.sqrt(new_G + eps)
    return (new_W, new_G)
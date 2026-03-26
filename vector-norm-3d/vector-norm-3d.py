import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v_ = np.array(v, dtype = float)
    v_ = v_ ** 2
    z = np.ones((3,))
    return np.sqrt(v_ @ z)
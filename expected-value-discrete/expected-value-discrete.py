import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    p = np.asarray(p, dtype = float)
    flag = (sum(p) == 1)
    
    if flag:
        return float(x @ p.T)
    else: raise ValueError("ValueError")

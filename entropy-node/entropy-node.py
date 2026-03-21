import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    C = len(y)
    if C == 0:
        return 0.0
    _, freqY = np.unique(y, return_counts = True)
    
    freqY = np.asarray(freqY, dtype = float)
    freqY /= sum(freqY)
    PY = freqY[freqY !=0]
    
    res = PY @ np.log2(PY.T)
    return float(-res)
    
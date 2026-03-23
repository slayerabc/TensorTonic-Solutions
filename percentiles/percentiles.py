import numpy as np
    
def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    x = np.sort(x)
    n = x.size
    q = (np.asarray(q, dtype = float)/100) * (n-1)

    low = q.astype(int)
    high = np.clip(low+1, 0, n-1)

    IQR = q - low

    return (1 - IQR) * x[low] + IQR * x[high]
    
    
    
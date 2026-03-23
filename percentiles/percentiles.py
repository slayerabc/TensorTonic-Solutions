import numpy as np

def compute(i, x, n):
    if (i == 0.0) | (i == float(n-1)): 
        return x[int(i)]

    IQR = x[int(i)+1] - x[int(i)] 
    
    return np.where(i == float(int(i)), x[int(i)], x[int(i)] + (i - int(i)) * IQR)
    

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    x = np.sort(x)
    n = x.size 
    q = (np.asarray(q, dtype = float)/100) * (n-1)


    return np.array([compute(i, x, n) for i in q])
import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf = np.array([p if x == 1 else 1-p for x in x])
    mean = p
    var = p * (1 - p)
    return (pmf, mean, var)
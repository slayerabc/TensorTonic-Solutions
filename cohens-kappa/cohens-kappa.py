import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    pass
    rater2 = np.asarray(rater2, dtype = float)
    rater1 = np.asarray(rater1, dtype = float)
    po = np.mean(rater1 == rater2)
    
    _, freq1 = np.unique(rater1, return_counts = True)
    freq1 = freq1/sum(freq1)
    
    _, freq2 = np.unique(rater2, return_counts = True)
    freq2 = freq2/sum(freq2)

    pe = freq1 @ freq2

        
    if pe == 1:
        return 1.0
    else: 
        return float((po-pe)/(1-pe))
        
    
    
    
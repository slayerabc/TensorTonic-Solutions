def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code here
    priorities = [p ** alpha for p in priorities]
    sum_ = sum(priorities)
    priorities = [p/sum_ for p in priorities]

    
    N = len(priorities)
    W = [(N * p) ** (-beta) for p in priorities]
    max_value = max(W)
    W_normalized = [w / max_value for w in W]

    
    return [priorities, W_normalized]
    
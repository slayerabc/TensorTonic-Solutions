def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    wr = [(R * v + min_votes * global_mean)/(v + min_votes) for R, v in items]
    return wr
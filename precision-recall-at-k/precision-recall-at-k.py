def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = []
    for i in range(0, min(len(recommended), k)):
        if(recommended[i] in relevant) & (recommended[i] not in top_k):
            top_k.append(recommended[i])
            
    precision = len(top_k) / k
    recall = len(top_k) / len(relevant)
    
    return [precision, recall]

    
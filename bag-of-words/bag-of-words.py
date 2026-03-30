import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    res = [tokens.count(word) for word in vocab]
    return np.asarray(res, dtype = int)
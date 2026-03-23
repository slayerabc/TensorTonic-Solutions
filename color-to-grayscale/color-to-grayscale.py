import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    x = np.array(image)
    color = np.array([0.299, 0.587, 0.114])
    res = x @ color
    return res.tolist()

    
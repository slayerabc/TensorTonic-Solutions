def derivative_f_x(a, b, x):
    return float(2*a*x + b)

def gradient_descent_quadratic(a, b, c, x, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for _ in range(steps):

        error = derivative_f_x(a, b, x)
        x -= lr * error

    return float(x)
    
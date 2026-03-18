import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    m_new = np.array(m)
    v_new = np.array(v)
    param_new = np.array(param)
    grad = np.asarray(grad)
    
    m_new = beta1 * m_new + (1 - beta1) * grad
    v_new = beta2 * v_new + (1 - beta2) * (grad**2)
    
    m_mean = m_new / (1 - beta1**t)
    v_mean = v_new / (1 - beta2**t)
    
    param_new = param_new - lr * m_mean / (np.sqrt(v_mean) + eps)
    
    return (param_new, m_new, v_new)
    
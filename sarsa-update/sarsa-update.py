def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here
    Q = q_table.copy()
    td_error = reward + gamma * Q[next_state][next_action] - Q[state][action]
    Q[state][action] += alpha * td_error

    return Q
    
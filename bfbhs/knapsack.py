import itertools as itt

def sum_of_values(values, key):
    """Calculates the weighted sum of a list of values based on a binary key.

    Parameters:
    - values (list): A list of numbers (weights or profits).
    - key (list): A binary list (0s and 1s) of the same size as `values`.
                  It acts as a selector, where 1 means include the value and 0 
                  means exclude it.

    Returns:
    - sum (int/float): The sum of the values from `values` where the 
    corresponding element in `key` is 1.
    """
    sum = 0
    n = len(values)
    for i in range(n):
        sum += values[i]*key[i]
    return sum

def knapsack_problem(weights, profits, capacity, goal):
    """Solves a version of the knapsack problem using brute force.
    It searches for a combination of items that meets a weight capacity and 
    achieves or exceeds a profit goal.

    Parameters:
    - weights (list): A list of numbers representing the weights of available 
    items.
    - profits (list): A list of numbers representing the profits of available 
    items, corresponding to the weights.
    - capacity (int/float): The maximum weight capacity of the knapsack.
    - goal (int/float): The minimum profit to be achieved.

    Returns:
    - sequence (tuple): A binary tuple representing the selection of items 
                    (1 for included, 0 for excluded)
                    that meets both weight and profit conditions. 
                    If multiple solutions exist, it returns the first one found.
    - False: If no combination of items is found that satisfies both conditions 
    (capacity and profit goal).
    """
    n = len(profits)
    sequences = itt.product([0, 1], repeat = n)
    for sequence in sequences:
        if sum_of_values(weights, sequence) <= capacity \
        and sum_of_values(profits, sequence) >= goal:
            return sequence
    return False
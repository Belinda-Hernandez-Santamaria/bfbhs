import itertools as itt
import networkx as nx

def is_hamiltonian_cycle(graph, cycle):
    #documentación (debe de estar inmediato a la definición de la función)
    """Checks if cycle is a hamiltonian cycle in graph.
    Graph is a Networkx graph, and cycle is a list of vertices. """
    n = len(set(cycle))
    if n != graph.order():
        return False
    for i in range(n-1):
        if not graph.has_edge(cycle[i], cycle[i+1]):
            return False
    if not graph.has_edge(cycle[n-1], cycle[0]):
        return False
    return True

def is_hamiltonian(graph):
    if not nx.is_connected(graph):
        return False
    vertices = list(graph.nodes)
    if len(vertices) < 3:  #Pues por convención un ciclo tiene al menos tres vértices
        return False
    perms = itt.permutations(vertices)
    for perm in perms:
        if is_hamiltonian_cycle(graph, perm):
            return perm
    return False

# Colorido de a tres 

def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]: # que color le corresponde a cada extremo de la lista, si ambos colores son iguales entonces es falso y por tanto no es propia
            return False
    return True

def is_3_coloring(graph):
    n = graph.order() # cantidad de vértices
    colorings = itt.product([0, 1, 2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring(graph, coloring):
            return coloring
    return False

#  Dora

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

def knapsack(weights, profits, capacity, goal):
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

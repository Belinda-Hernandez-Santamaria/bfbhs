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

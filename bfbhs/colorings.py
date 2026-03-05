import itertools as itt

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
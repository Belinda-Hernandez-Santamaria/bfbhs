from bfbhs import is_3_coloring
from itertools import product
import networkx as nx
atlas = nx.graph_atlas_g()
g= nx.cubical_graph()
def test_is_3_coloring():
    assert is_3_coloring(g) == (0, 1, 0, 1, 1, 0, 1, 0)
    assert is_3_coloring(atlas[102]) == (0, 0, 1, 2, 1, 1)
    assert is_3_coloring(atlas[1200]) == False
    assert is_3_coloring(atlas[1209]) == False
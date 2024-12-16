import pytest
from graph import Graph
from coloring import graph_coloring

@pytest.mark.parametrize(
    "config",
    [
        #n, edges, expected_answer
        (4, [(0, 1), (1, 2), (2, 3)], [1, 2, 1, 2]),
        (4, [(0, 1), (0, 2), (0, 3)], [1, 2, 2, 2]),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0)], [1, 2, 1, 2]),
        (7, [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)], [2, 1, 4, 2, 2, 5, 5]),
        (5, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2)], [2, 3, 1, 2, 3]),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (0, 3)], [1, 2, 3, 2, 3]),
        (6, [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], [1, 4, 4, 2, 2, 2]),
        (12, [(0, 1), (1, 2), (2, 5), (4, 5), (3, 4), (3, 6), (6, 7), (7, 8), (6, 9), (7, 10), (8, 11), (9, 10), (10, 11)], [1, 2, 1, 1, 2, 3, 2, 1, 2, 1, 2, 1])
    ]
)

def test_coloring(config):
    n, edges, expected = config
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)

    colors = graph_coloring(g)
    assert colors == expected
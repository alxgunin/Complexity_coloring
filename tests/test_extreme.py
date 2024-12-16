import pytest
from graph import Graph
from coloring import graph_coloring

@pytest.mark.parametrize(
    "config",
    [
        (1, [], [1]),
        (2, [], [1, 1]),
        (2, [(0, 1)], [1, 2]),
        (3, [], [1, 1, 1]),
        (3, [(0, 1)], [1, 2, 1]),
        (3, [(0, 1), (1, 2)], [2, 1, 2]),
        (3, [(0, 1), (1, 2), (0, 2)], [1, 2, 3]),
        (10, [], [1] * 10),
        (100, [], [1] * 100),
        (1000, [], [1] * 1000),
        (10_000, [], [1] * 10_000),
    ]
)
def test_coloring(config):
    n, edges, expected = config
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)

    colors = graph_coloring(g)
    assert colors == expected
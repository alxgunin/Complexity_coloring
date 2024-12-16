import pytest
from graph import Graph
from coloring import graph_coloring
from itertools import product

@pytest.mark.parametrize(
    "size",
    [
        100,
        300,
        500,
        1000,
        5_000,
    ]
)
def test_3n_graph(size):
    g = Graph(3 * size)
    for n in range(size):
        g.add_edge(n * 3, n * 3 + 1)
        g.add_edge(n * 3, n * 3 + 2)
        g.add_edge(n * 3 + 1, n * 3 + 2)
    
    colors = graph_coloring(g)
    assert colors == [1, 2, 3] * size


@pytest.mark.parametrize(
    "size",
    [
        100,
        300,
        500,
        1000,
        10_000,
    ]
)
def test_star_graph(size):
    g = Graph(size)
    for n in range(1, size):
        g.add_edge(0, n)
    
    colors = graph_coloring(g)
    assert colors == [1] + [2] * (size - 1)


@pytest.mark.parametrize(
    "size_1, size_2",
    product(
        [100, 300, 500, 1000, 5_000],
        [100, 300, 500, 1000, 5_000],
    )
)
def test_bipartite_graph(size_1, size_2):
    g = Graph(size_1 + size_2)
    for i in range(size_1):
        for j in range(size_2):
            g.add_edge(i, size_1 + j)
    
    colors = graph_coloring(g)
    assert (colors == [1] + [4] * (size_1 - 1) + [2] * size_2) or (colors == [2] * size_1 + [1] + [4] * (size_2 - 1))

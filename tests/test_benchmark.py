import pytest
from graph import Graph
from coloring import graph_coloring
from itertools import product
import numpy as np


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
def test_3n_graph(size, benchmark):
    g = Graph(3 * size)
    for n in range(size):
        g.add_edge(n * 3, n * 3 + 1)
        g.add_edge(n * 3, n * 3 + 2)
        g.add_edge(n * 3 + 1, n * 3 + 2)
    
    benchmark(graph_coloring, g)


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
def test_star_graph(size, benchmark):
    g = Graph(size)
    for n in range(1, size):
        g.add_edge(0, n)
    
    benchmark(graph_coloring, g)


@pytest.mark.parametrize(
    "height, width",
    product(
        [1, 2, 5, 10, 30, 50],
        [1, 2, 5, 10, 30, 50],
    )
)
def test_grid_graph(height, width, benchmark):
    g = Graph(width * height)
    for i in range(height - 1):
        for j in range(width - 1):
            g.add_edge(i * width + j, i * width + j + 1)
            g.add_edge(i * width + j, (i + 1) * width + j)

    for i in range(width - 1):
        g.add_edge((height - 1) * width + i, (height - 1) * width + i + 1)
    
    for j in range(height - 1):
        g.add_edge(width - 1 + j * width, width - 1 + (j + 1) * width)

    benchmark(graph_coloring, g)


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
def test_line_graph(size, benchmark):
    g = Graph(size)
    for n in range(size - 1):
        g.add_edge(n, n + 1)
    
    benchmark(graph_coloring, g)

@pytest.mark.parametrize(
    "size_1, size_2",
    product(
        [100, 300, 500, 1000, 5_000],
        [100, 300, 500, 1000, 5_000],
    )
)
def test_bipartite_graph(size_1, size_2, benchmark):
    g = Graph(size_1 + size_2)
    for i in range(size_1):
        for j in range(size_2):
            g.add_edge(i, size_1 + j)
    
    benchmark(graph_coloring, g)


@pytest.mark.parametrize(
    "prob, size",
    product(
        [0.1, 0.3, 0.5, 0.7, 0.9],
        [10, 100, 500, 1000],
    )
)
def test_prob_graph(prob, size, benchmark):
    g = Graph(size * 3)
    for i in range(size):
        for j in range(size):
            if np.random.binomial(n=1, p=prob):
                g.add_edge(i, size + j)

    for i in range(size):
        for j in range(size):
            if np.random.binomial(n=1, p=prob):
                g.add_edge(i, 2 * size + j)
    
    for i in range(size):
        for j in range(size):
            if np.random.binomial(n=1, p=prob):
                g.add_edge(size + i, 2 * size + j)

    benchmark(graph_coloring, g)

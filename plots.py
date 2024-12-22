import pytest
import time
import matplotlib.pyplot as plt
import numpy as np

from coloring import graph_coloring
from graph import Graph


def draw_results(x, y, name):
    plt.plot(x, y, label=name)
    plt.title("Benchmark results")
    plt.ylabel("Execution time, sec")
    plt.xlabel("Graph size")
    plt.grid()
    plt.legend()
    plt.show()


def plot_3n_graph():
    results = []
    sizes = np.linspace(300, 5000, 15, dtype=int)

    for size in sizes:
        g = Graph(3 * size)
        for n in range(size):
            g.add_edge(n * 3, n * 3 + 1)
            g.add_edge(n * 3, n * 3 + 2)
            g.add_edge(n * 3 + 1, n * 3 + 2)

        begin = time.time()
        graph_coloring(g)
        end = time.time()
        results.append(end - begin)

    draw_results(sizes, results, "triangle graph")


def plot_star_graph():
    results = []
    sizes = np.linspace(300, 10_000, 15, dtype=int)

    for size in sizes:
        g = Graph(size)
        for n in range(1, size):
            g.add_edge(0, n)

        begin = time.time()
        graph_coloring(g)
        end = time.time()
        results.append(end - begin)

    draw_results(sizes, results, "star graph")


def plot_grid_graph():
    results = []
    sizes = np.linspace(1, 50, 15, dtype=int)
    for width in sizes:
            height = width
            g = Graph(width * height)
            for i in range(height - 1):
                for j in range(width - 1):
                    g.add_edge(i * width + j, i * width + j + 1)
                    g.add_edge(i * width + j, (i + 1) * width + j)

            for i in range(width - 1):
                g.add_edge((height - 1) * width + i, (height - 1) * width + i + 1)
            
            for j in range(height - 1):
                g.add_edge(width - 1 + j * width, width - 1 + (j + 1) * width)

            begin = time.time()
            graph_coloring(g)
            end = time.time()
            results.append(end - begin)

    draw_results(sizes, results, "grid graph(width = height)")


def plot_line_graph():
    results = []
    sizes = np.linspace(300, 5000, 15, dtype=int)

    for size in sizes:
        g = Graph(size)
        for n in range(size - 1):
            g.add_edge(n, n + 1)
        
        begin = time.time()
        graph_coloring(g)
        end = time.time()
        results.append(end - begin)
    
    draw_results(sizes, results, "line graph")


def plot_bipartite_graph():
    results = []
    sizes = np.linspace(100, 5000, 15, dtype=int)

    for size in sizes:
        size_1, size_2 = size, size
        g = Graph(size_1 + size_2)
        for i in range(size_1):
            for j in range(size_2):
                g.add_edge(i, size_1 + j)

        begin = time.time()
        graph_coloring(g)
        end = time.time()
        results.append(end - begin)

    draw_results(sizes, results, "bipartite symmetric graph")


def plot_prob_graph():
    results = []
    sizes = np.linspace(100, 5000, 15, dtype=int)
    prob = 0.3

    for size in sizes:
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

        begin = time.time()
        graph_coloring(g)
        end = time.time()
        results.append(end - begin)

    draw_results(sizes, results, "probability graph")


# plot_3n_graph()
# plot_star_graph()
# plot_grid_graph()
# plot_line_graph()
# plot_bipartite_graph()
# plot_prob_graph()
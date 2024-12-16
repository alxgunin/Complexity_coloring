import pytest
from graph import Graph

def test_edge():
    g = Graph(2)
    assert g.get_size() == 2
    assert [] == g.get_neighbors(0)

    g.add_edge(0, 1)
    assert [1] == g.get_neighbors(0)

    g.remove_edge(0, 1)
    assert [] == g.get_neighbors(0)

def test_color():
    g = Graph(1)
    assert g.get_size() == 1

    assert None == g.get_color(0)

    g.set_color(0, 123)
    assert 123 == g.get_color(0)
    
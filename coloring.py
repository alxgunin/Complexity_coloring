from graph import Graph

def graph_coloring(g: Graph) -> list[int]:
    removed = [False for _ in range(g.get_size())]
    next_color = 1
    while True:
        max_degree = 0
        vertex_max_degree = -1
        for v in range(g.get_size()):
            if not removed[v]:
                count = 0
                for u in g.get_neighbors(v):
                    if not removed[u]:
                        count += 1
                 
                if max_degree < count:
                    max_degree = count
                    vertex_max_degree = v

        if max_degree ** 2 <= g.get_size():
            for v in range(g.get_size()):
                if g.get_color(v) is None:
                    current_color = next_color
                    while True:
                        ok = True
                        for u in g.get_neighbors(v):
                            if removed[u]:
                                continue
                            other_color = g.get_color(u)
                            if other_color is not None and other_color == current_color:
                                ok = False
                                break
                        if ok:
                            g.set_color(v, current_color)
                            break
                        else:
                            current_color += 1
            break
        else:
            g.set_color(vertex_max_degree, next_color)
            next_color += 1
            neighbors = g.get_neighbors(vertex_max_degree)

            for u in neighbors:
                if not removed[u]:
                    use_next_color = True
                    for v in g.get_neighbors(u):
                        if not removed[v]:
                            color = g.get_color(v)
                            if color is not None and color == next_color:
                                use_next_color = False
                                break

                    g.set_color(u, next_color if use_next_color else next_color + 1)

            next_color += 2
            removed[vertex_max_degree] = True
            for u in neighbors:
                removed[u] = True

    return [g.get_color(i) for i in range(g.get_size())]
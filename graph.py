class Graph:
    def __init__(self, n = 0) -> None:
        self.n = n
        self.matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
        self.coloring: list[None | int] = [None for _ in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self, u: int, v: int) -> None:
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def set_color(self, v: int, color: int) -> None:
        self.coloring[v] = color
    
    def get_size(self) -> int:
        return self.n
    
    def get_neighbors(self, v: int) -> list[int]:
        result = []
        for u, connected in enumerate(self.matrix[v]):
            if connected:
                result.append(u)
        return result

    def get_color(self, v: int) -> int | None:
        return self.coloring[v]
    
import math
import time

import networkx as nx
from Problem81 import parse

"""
naive O(n^2 * n^2) complexity algorithm: compute shortest paths for all target-source pairs (slow)

better: O(n * n^2) complexity algorithm: Add a vertex s with cost 0 that is connected to all source vertices and a vertex t with cost 0 that is connected to all target vertices
        then perform single iteration of dijkstra from s to t to get answer

"""

def build_graph(matrix):
        n = len(matrix)
        G = nx.Graph()
        for y in range(n):
            for x in range(n):
                node = (y, x)
                if y > 0:  # top
                    w = 0.5 * (matrix[y - 1][x] + matrix[y][x])
                    G.add_edge(node, (y - 1, x), weight=w)
                if y < n - 1:  # bottom
                    w = 0.5 * (matrix[y + 1][x] + matrix[y][x])
                    G.add_edge(node, (y + 1, x), weight=w)
                if x > 0:  # left
                    pass   # adding these edges wouldn't change anything since an optimal solution would never go left anyway
                if x < n - 1:  # right
                    w = 0.5 * (matrix[y][x + 1] + matrix[y][x])
                    G.add_edge(node, (y, x + 1), weight=w)
        return G


def solve():
    m = parse()
    G = build_graph(m)
    n = len(m)

    path_weight = math.inf
    for i in range(n):
        for j in range(n):
            path = nx.shortest_path(G, source=(i, 0), target=(j, n - 1), weight='weight')
            path_weight = min(path_weight, sum(m[r][c] for (r, c) in path))

    print(f"Shortest path weight: {path_weight}")


def solve2():
    m = parse()
    n = len(m)
    G = build_graph(m)

    s = (-1, -1)
    t = (n, n)

    for i in range(n):
        G.add_edge(s, (i, 0), weight=0)
        G.add_edge(t, (i, n - 1), weight=0)

    path = nx.shortest_path(G, source=s, target=t, weight='weight')
    path.pop()
    path.pop(0)
    path_weight = sum(m[r][c] for (r, c) in path)

    print(f"Shortest path weight: {path_weight}")


if __name__ == '__main__':
    start = time.monotonic()
    solve2()
    end = time.monotonic()
    print(f"Duration: {(end - start)} s")

    start = time.monotonic()
    solve()
    end = time.monotonic()
    print(f"Duration: {(end - start)} s")

from Problem81 import parse
import networkx as nx

"""
We reduce to the problem to Dijkstra by setting up edge weights w: V --> R, w(u, v) = 0.5 * (c(u) + c(v))

Intuition: We pay for every vertex on the way in and on the way out.
"""

def solve():
    matrix = parse()
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
                w = 0.5 * (matrix[y][x - 1] + matrix[y][x])
                G.add_edge(node, (y, x - 1), weight=w)
            if x < n - 1:  # right
                w = 0.5 * (matrix[y][x + 1] + matrix[y][x])
                G.add_edge(node, (y, x + 1), weight=w)

    path = nx.shortest_path(G, source=(0, 0), target=(n - 1, n - 1), weight='weight')
    path_weight = sum(matrix[r][c] for (r, c) in path)

    print(f"Shortest path: {path}")
    print(f"Total path weight: {path_weight}")


if __name__ == '__main__':
    solve()


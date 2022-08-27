"""
********************************Count the Connected Components********************************
Algorithm:
* Formatting --> Convert the given edges to the adjacency list
* Next approach will be iterative + DFS (recursive)
* In DFS, for a particular source vertex, we will visit as deep as we can go and mark each vertex as seen/visited.
    -> When a particular connected graph is visited, we return True
* In the iterative section, we loop through the keys of the adjacency list and run dfs for each key.
    -> If DFS return True for each key, which means we have found one connected graph and increase the count.
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def draw_graph(self, edges):
        for edge in edges:
            if len(edge) == 1:
                v, = edge
                self.adj_list[v] = []
            else:
                v1, v2 = edge
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)

    def count_connected_components(self):
        count = 0
        visited = set()

        def dfs(src, seen):
            if src in seen:
                return False
            seen.add(src)

            for neighbour in self.adj_list[src]:
                dfs(neighbour, seen)
            return True

        for vertex in self.adj_list:
            if dfs(vertex, visited):
                count += 1

        return count


edges = [
    [1, 2],
    [4, 6],
    [5, 6],
    [6, 8],
    [6, 7],
    [3]
]

my_graph = Graph()
my_graph.draw_graph(edges)
print(my_graph.adj_list)

print(my_graph.count_connected_components())

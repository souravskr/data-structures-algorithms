from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def draw_graph(self, edges):
        for v1, v2 in edges:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def shortest_path(self, source, destination):
        visited = set(source)
        queue = [(source, 0)]
        while queue:
            cur_vertex, distance = queue.pop(0)
            if cur_vertex == destination:
                return distance

            for neighbour in self.adj_list[cur_vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, distance+1))
        return -1


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

my_graph = Graph()
my_graph.draw_graph(edges)
print(my_graph.adj_list)
print(my_graph.shortest_path('w', 'z'))

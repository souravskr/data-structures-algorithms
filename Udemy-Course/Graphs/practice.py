"""
Graph defines a relationship between things. Such as:
Nodes --> Cities
Edges --> Roads
Relation --> Roads connect cities.

Nodes --> Courses
Edges --> Pre-requisites
Relation --> In order to register a course, we must complete the pre-requisites.

Directed Graph (One Way) & Undirected Graph (Two way)

Terminology: Neighbour Node of a node.

Adjacency List: {
        a: [b, c],
        b: [d],
        c: [e],
        d: [],
        e: [b],
        f: [d]
    }
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, val):
        if val not in self.adj_list:
            self.adj_list[val] = []
            return True
        return False

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex in self.adj_list and end_vertex in self.adj_list:
            self.adj_list[start_vertex].append(end_vertex)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
        return False

    def remove_vertex(self, v):
        if v in self.adj_list:
            for vertex in self.adj_list[v]:
                self.adj_list[vertex].remove(v)
            del self.adj_list[v]
            return True
        return False

    def dfs_iterative(self, start_vertex):
        res = []
        if self.adj_list is None:
            return res
        stack = [start_vertex]
        while stack:
            cur_vertex = stack.pop()
            res.append(cur_vertex)
            if self.adj_list[cur_vertex]:
                stack.extend(self.adj_list[cur_vertex])
        return res

    def dfs(self, start_vertex):
        res = []

        def traverse(source):
            res.append(source)
            for vertex in self.adj_list[source]:
                traverse(vertex)
        traverse(start_vertex)
        return res

    def bfs(self, start_vertex):
        res = []
        if self.adj_list is None:
            return res
        queue = [start_vertex]
        while queue:
            cur_vertex = queue.pop(0)
            res.append(cur_vertex)
            if self.adj_list[cur_vertex]:
                queue.extend(self.adj_list[cur_vertex])
        return res


my_graph = Graph()
my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.add_vertex('c')
my_graph.add_vertex('d')
my_graph.add_vertex('e')
my_graph.add_vertex('f')
my_graph.add_edge('a', 'b')
my_graph.add_edge('a', 'c')
my_graph.add_edge('b', 'd')
my_graph.add_edge('c', 'e')
my_graph.add_edge('d', 'f')
print('Graph(Adjacency List): ', my_graph.adj_list)

print('DFS-Iterative: ', my_graph.dfs_iterative('a'))
print('DFS-Recursive: ', my_graph.dfs('a'))
print('BFS: ', my_graph.bfs('a'))

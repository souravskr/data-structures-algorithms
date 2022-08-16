class Graph:
    def __init__(self):
        self.add_list = {}

    def print_graph(self):
        for vertex, vertices in self.add_list.items():
            print(f'{vertex} : {vertices}')

    def add_vertex(self, vertex):
        if vertex not in self.add_list:
            self.add_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.add_list and v2 in self.add_list:
            self.add_list[v1].append(v2)
            self.add_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.add_list and v2 in self.add_list:
            self.add_list[v1].remove(v2)
            self.add_list[v2].remove(v1)
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_edge('A', 'B')
my_graph.print_graph()
my_graph.remove_edge('A', 'B')
my_graph.print_graph()

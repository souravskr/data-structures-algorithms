class Graph:
    def __init__(self):
        self.adj_list = {
            1: [0],
            5: [8, 0],
            0: [5, 8],
            8: [5, 0],
            4: [2, 3],
            3: [4, 2],
            2: [4, 3]
        }

    def largest_component(self):
        visited = set()
        largest_size = 0

        def dfs(src, seen):
            if src in seen:
                return 0
            seen.add(src)
            count = 1
            for neighbour in self.adj_list[src]:
                count += dfs(neighbour, seen)
            return count

        for vertex in self.adj_list:
            size = dfs(vertex, visited)
            largest_size = max(size, largest_size)

        return largest_size


my_graph = Graph()
print(my_graph.adj_list)
print(my_graph.largest_component())

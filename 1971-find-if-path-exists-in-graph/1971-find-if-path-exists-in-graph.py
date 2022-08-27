class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def build_graph(edges):
            adj_list = {}
            for edge in edges:
                a, b = edge
                if a not in adj_list:
                    adj_list[a] = []
                if b not in adj_list:
                    adj_list[b] = []
                adj_list[a].append(b)
                adj_list[b].append(a)
            return adj_list


        adj_list = build_graph(edges)
        
        def dfs_undirected(graph, src, dst, visited):
            if src == dst:
                return True
            if src in visited:
                return False
            visited.add(src)
            for vertex in graph[src]:
                if dfs_undirected(graph, vertex, dst, visited):
                    return True
            return False
        
        return dfs_undirected(adj_list, source, destination, set())
        
        
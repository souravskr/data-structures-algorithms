# edges = [
#     ['i', 'j'],
#     ['k', 'i'],
#     ['m', 'k'],
#     ['k', 'l'],
#     ['o', 'n']
# ]
from collections import defaultdict

edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]


# adj_list = {}
# for i in range(len(edges)):
#     for j in range(len(edges[i]) - 1):
#         if edges[i][j] in adj_list:
#             adj_list[edges[i][j]].append(edges[i][j + 1])
#         else:
#             adj_list[edges[i][j]] = [edges[i][j + 1]]
#         if edges[i][j + 1] in adj_list:
#             adj_list[edges[i][j + 1]].append(edges[i][j])
#         else:
#             adj_list[edges[i][j + 1]] = [edges[i][j]]

# print(adj_list)


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
print(adj_list)


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


print(dfs_undirected(adj_list, 0, 5, set()))


def valid_path_for_undirected_graph(edges, source, destination):
    adj_list = defaultdict(list)
    for v1, v2 in edges:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    def dfs(src, dst, visited):
        if src == dst:
            return True
        if src in visited:
            return False

        visited.add(src)

        for vertex in adj_list[src]:
            if dfs(vertex, dst, visited):
                return True
        return False

    visited = set()
    return dfs(source, destination, visited)


print(valid_path_for_undirected_graph(edges, 0, 5))

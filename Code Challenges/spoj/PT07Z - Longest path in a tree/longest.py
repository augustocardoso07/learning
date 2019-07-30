def max_path(nodes, n, start):
    neighbors = [(start, 0)]
    visited = [False] * n

    maxpath = 0
    maxv = 0

    while len(neighbors) != 0:
        v, path_distance = neighbors.pop()
        visited[v] = True

        if len(nodes[v]) == 1 and v != start and path_distance > maxpath:
            maxv, maxpath = v, path_distance

        for u in nodes[v]:
            if not visited[u]:
                neighbors.append((u, path_distance + 1))

    return maxv, maxpath



n = int(input())

nodes = [[] for _ in range(n)]

for _ in range(n - 1):
    v, u = [int(x) - 1 for x in input().split()]
    nodes[v].append(u)
    nodes[u].append(v)

v, _ = max_path(nodes, n, 0)
_, result = max_path(nodes, n, v)
print(result)
def connected(nodes, n):
    root = 0
    neighbors = [root]
    visited = [False] * n

    while len(neighbors) != 0:
        v = neighbors.pop()
        visited[v] = True

        for u in nodes[v]:
            if not visited[u]:
                neighbors.append(u)

    return sum(visited) == n


n, m = [int(x) for x in input().split()]

nodes = [[] for _ in range(n)]

for _ in range(m):
    v, u = [int(x) - 1 for x in input().split()]
    nodes[v].append(u)
    nodes[u].append(v)

is_tree = m == (n - 1) and connected(nodes, n)

print("YES") if is_tree else print("NO")
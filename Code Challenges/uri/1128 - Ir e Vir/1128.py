def dfs(n, v, graph):
    stack = [v]
    visited = [False] * n
    visited[v] = True

    while stack:
        v = stack.pop()

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)

    return sum(visited) == n


def solve(n, nodes, inverted_nodes):
    connect = dfs(n, 0, nodes)
    if not connect: return 0

    connect = dfs(n, 0, inverted_nodes)
    return int(connect)


def main():
    while True:
        n, m = [int(x) for x in input().split()]
        if n == 0 or m == 0: break

        nodes = [[] for _ in range(n)]
        inverted_nodes = [[] for _ in range(n)]
        for _ in range(m):
            v, u, p = [int(x) - 1 for x in input().split()]
            nodes[v].append(u)
            inverted_nodes[u].append(v)
            if p == 1:
                nodes[u].append(v)
                inverted_nodes[v].append(u)

        result = solve(n, nodes, inverted_nodes)
        print(result)


if __name__ == '__main__':
    main()

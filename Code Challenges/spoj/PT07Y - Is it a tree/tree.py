def connected(nodes, n):
    root = 0
    neighbors = [root]
    visited = [False] * n
    visited[root] = True

    while len(neighbors) != 0:
        v = neighbors.pop()

        for u in nodes[v]:
            if not visited[u]:
                neighbors.append(u)
                visited[u] = True

    return sum(visited) == n


def main():
    n, m = [int(x) for x in input().split()]

    nodes = [[] for _ in range(n)]

    for _ in range(m):
        v, u = [int(x) - 1 for x in input().split()]
        nodes[v].append(u)
        nodes[u].append(v)

    is_tree = m == (n - 1) and connected(nodes, n)

    print("YES") if is_tree else print("NO")


if __name__ == '__main__':
    main()
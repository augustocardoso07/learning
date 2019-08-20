def max_path(nodes, n, start):
    neighbors = [(start, 0)]
    visited = [False] * n
    visited[start] = True


    maxpath = 0
    maxv = 0

    while neighbors:
        v, path_distance = neighbors.pop()

        if path_distance > maxpath:
            maxv, maxpath = v, path_distance

        for u in nodes[v]:
            if not visited[u]:
                neighbors.append((u, path_distance + 1))
                visited[v] = True

    return maxv, maxpath


def main():
    n = int(input())

    nodes = [[] for _ in range(n)]

    for _ in range(n - 1):
        v, u = [int(x) - 1 for x in input().split()]
        nodes[v].append(u)
        nodes[u].append(v)

    v, _ = max_path(nodes, n, 0)
    _, result = max_path(nodes, n, v)
    print(result)


if __name__ == '__main__':
    main()
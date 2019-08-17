def dfs(files, v, n):
    visited = [False] * n
    visited[v] = True
    stack = [(v, 1)]

    m = 0
    while stack:
        v, size = stack.pop()
        if size > m: m = size

        for u in files[v]:
            if not visited[u]:
                stack.append((u, size + 1))
                visited[u] = True
    return m


def dfsr_util(files, v, visited, status, nivel):
    if visited[v]: return
    visited[v] = True
    status[v] = True
    m = 0
    for u in files[v]:
        if not visited[u]:
            m = dfsr_util(files, u, visited, status, nivel + 1)
        else:
            if status[u]:
                raise ConnectionError

    status[v] = False
    return max(m, nivel)


def dfsr(files, v, n):
    visited = [False] * n
    status = [False] * n
    try:
        return dfsr_util(files, v, visited, status, 1)
    except ConnectionError:
        return -1


def solve(files, n):
    total = 0
    for v in range(n):
        m = dfsr(files, v, n)
        if m > total: total = m
        if m == -1:
            total = -1
            break
    return total


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        files = []
        for i in range(n):
            m, *rest = [int(x) - 1 for x in input().split()]
            files.append(rest)

        result = solve(files, n)
        print(result)


if __name__ == '__main__':
    main()


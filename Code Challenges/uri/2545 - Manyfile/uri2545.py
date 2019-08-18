ENTER = 1
EXIT = 0


def dfs(files, v, n):
    visited = [False] * n
    visited[v] = True
    stack = [(v, 1, ENTER)]
    status = [False] * n

    m = 0
    while stack:
        v, size, action = stack.pop()
        if size > m: m = size

        if action == EXIT:
            status[v] = False
        else:
            status[v] = True
            stack.append((v, size, EXIT))
            for u in files[v]:
                if not visited[u]:
                    stack.append((u, size + 1, ENTER))
                    visited[u] = True
                elif status[u]: return -1
    return m


def solve(files, n):
    total = 0
    for v in range(n):
        m = dfs(files, v, n)
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

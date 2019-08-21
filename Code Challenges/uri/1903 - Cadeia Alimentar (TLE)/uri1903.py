ENTER = 1
EXIT = 0


def dfs(cadeia, v, n):
    visited = [False] * n
    visited[v] = True
    stack = [(v, ENTER)]
    status = [False] * n

    while stack:
        v, action = stack.pop()

        if action == EXIT:
            status[v] = False
        else:
            status[v] = True
            stack.append((v, EXIT))
            for u in cadeia[v]:
                if not visited[u]:
                    stack.append((u, ENTER))
                    visited[u] = True
                elif status[u]: return True
    return False


def solve(cadeia, cadeia_invert, n):
    return dfs(cadeia, 0, n) or dfs(cadeia_invert, 0, n)


def main():
    n, m = [int(x) for x in input().split()]
    cadeia = [[] for _ in range(n)]
    cadeia_invert = [[] for _ in range(n)]
    for _ in range(m):
        u, v = [int(x) - 1 for x in input().split()]
        cadeia[v].append(u)
        cadeia_invert[u].append(v)

    if solve(cadeia, cadeia_invert, n):
        print("Bolada")
    else:
        print("Nao Bolada")


if __name__ == '__main__':
    main()
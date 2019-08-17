def dfs(v, familias, visitado):
    parentes = [v]
    visitado[v] = True

    while len(parentes) != 0:
        v = parentes.pop()

        for u in familias[v]:
            if not visitado[u]:
                visitado[u] = True
                parentes.append(u)


def solve(familias, visitado, n):
    count = 0
    for v in range(n):
        if not visitado[v]:
            count += 1
            dfs(v, familias, visitado)

    return count


def main():
    n, m = [int(x) for x in input().split()]

    familias = [[] for _ in range(n)]
    visitado = [False] * n

    for _ in range(m):
        v, u = [int(x) - 1 for x in input().split()]
        familias[v].append(u)
        familias[u].append(v)

    result = solve(familias, visitado, n)
    print(result)


if __name__ == '__main__':
    main()


def test_in1(capsys):
    import sys
    sys.stdin = open("in1")
    main()
    out, err = capsys.readouterr()
    assert out == "1\n"
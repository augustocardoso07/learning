n, m = [int(x) for x in input().split()]

familias = [[] for _ in range(n)]
visitado = [False] * n

for _ in range(m):
    v, u = [int(x) - 1 for x in input().split()]
    familias[v].append(u)
    familias[u].append(v)

cout = 0


def dfs(v):
    parentes = [v]

    while len(parentes) != 0:
        v = parentes.pop()
        visitado[v] = True
        for u in familias[v]:
            if not visitado[u]:
                parentes.append(u)


for v in range(n):
    if not visitado[v]:
        cout += 1
        dfs(v)

print(cout)
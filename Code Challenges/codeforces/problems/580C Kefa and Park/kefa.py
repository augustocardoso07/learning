def eh_restaurante(v):
    return len(park[v]) == 1 and v > 0


def dfs(v, park, gatos, n, m):
    parentes = [(v, gatos[v])]
    result = 0
    visitados = [False] * n

    while len(parentes) != 0:
        v, gatos_consecutivos = parentes.pop()
        visitados[v] = True
        if eh_restaurante(v) and gatos_consecutivos <= m:
            result += 1
        else:
            for u in park[v]:
                if not visitados[u] and gatos_consecutivos <= m:
                    if gatos[u] == 0:
                        parentes.append((u, 0))
                    else:
                        parentes.append((u, gatos_consecutivos + gatos[u]))
    return result


n, m = [int(x) for x in input().split()]
gatos = [int(x) for x in input().split()]
park = [[] for _ in range(n)]

for _ in range(n - 1):
    v, u = [int(x) - 1 for x in input().split()]
    park[v].append(u)
    park[u].append(v)

result = dfs(0, park, gatos, n, m)
print(result)
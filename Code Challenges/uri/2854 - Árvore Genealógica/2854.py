def dfs(v, d):
    parentes = [v]
    visitados = set()
    while len(parentes) != 0:
        v = parentes.pop()
        visitados.add(v)
        for u in d[v]:
            if u not in visitados:
                parentes.append(u)
    return visitados


m, n = [int(x) for x in input().split()]

d = dict()

for _ in range(n):
    a, relacao, b = input().split()
    d[a] = d.get(a, []) + [b]
    d[b] = d.get(b, []) + [a]

count = 0
visitados = set()

for key, value in d.items():
    if key not in visitados:
        familia = dfs(key, d)
        visitados = visitados.union(familia)
        count += 1
print(count)
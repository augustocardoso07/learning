def read_nm():
    linha = input().split()
    if len(linha) == 1:
        n = int(linha[0])
        m = int(input())
    else:
        n, m = [int(x) for x in linha]
    return n, m

def dfs(v, visitados, pontos):
    vizinhos = [v]

    while len(vizinhos) != 0:
        v = vizinhos.pop()
        visitados[v] = True

        for u in pontos[v]:
            if not visitados[u]:
                vizinhos.append(u)


t = int(input())

for i in range(1, t + 1):
    n, m = read_nm()

    pontos = [[] for _ in range(n)]
    visitados = [False] * n
    for _ in range(m):
        x, y = [int(x) - 1 for x in input().split()]
        pontos[x].append(y)
        pontos[y].append(x)

    count = 0

    for v in range(n):
        if not visitados[v]:
            dfs(v, visitados, pontos)
            count += 1

    result = count - 1
    if result == 0:
        print("Caso #{}: a promessa foi cumprida".format(i))
    else:
        print("Caso #{}: ainda falta(m) {} estrada(s)".format(i, result))

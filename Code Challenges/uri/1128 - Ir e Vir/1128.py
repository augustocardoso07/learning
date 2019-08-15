def dfs(n, v, graph):
    vizinhos = [(v, 0)]
    visitados = [False] * n
    ultimo = 0
    max_distancia = 0
    visitados[v] = True

    while vizinhos:
        v, distancia = vizinhos.pop()
        if distancia > max_distancia: ultimo = v

        for u in graph[v]:
            if not visitados[u]:
                visitados[u] = True
                vizinhos.append((u, distancia + 1))

    return sum(visitados) == n, ultimo


def solve(n, inters, invert_inters):
    connect, ultimo = dfs(n, 0, inters)
    if not connect: return 0

    connect, _ = dfs(n, ultimo, invert_inters)
    return int(connect)


def main():
    while True:
        n, m = [int(x) for x in input().split()]
        if n == 0 or m == 0: break
        inters = [[] for _ in range(n)]
        invert_inters = [[] for _ in range(n)]
        for _ in range(m):
            v, w, p = [int(x) - 1 for x in input().split()]
            inters[v].append(w)
            invert_inters[w].append(v)
            if p == 1:
                inters[w].append(v)
                invert_inters[v].append(w)

        result = solve(n, inters, invert_inters)
        print(result)


if __name__ == '__main__':
    main()

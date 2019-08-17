from queue import PriorityQueue


def dijkstra(cidades, n, cidade_succa, cidade_noic):
    distancias = [float("inf")] * n
    visitados = [False] * n

    distancias[cidade_succa] = 0

    fila = PriorityQueue()

    fila.put((0, cidade_succa))

    while not fila.empty():
        dist, cidade = fila.get()
        if visitados[cidade]: continue

        visitados[cidade] = True

        for novadist, vizinho in cidades[cidade]:
            if not visitados[vizinho] and abs(dist + novadist) < distancias[vizinho]:
                distancias[vizinho] = abs(dist + novadist)
                fila.put((dist + novadist, vizinho))

    print(distancias)
    return distancias[cidade_noic]


def main():
    n, m = [int(x) for x in input().split()]
    cidade_succa, cidade_noic = [int(x) - 1 for x in input().split()]

    cidades = [[] for _ in range(n)]

    for _ in range(m):
        x, y, tempo = [int(x) for x in input().split()]
        cidades[x-1].append((tempo, y-1))
        cidades[y-1].append((tempo, x-1))

    result = dijkstra(cidades, n, cidade_succa, cidade_noic)
    print(result)


main()
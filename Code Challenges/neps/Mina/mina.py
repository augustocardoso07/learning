from queue import PriorityQueue


deslocamento = (
    (-1,  0),
    ( 1,  0),
    ( 0,  1),
    ( 0, -1)
)


def possivel(i, j, n):
    return 0 <= i < n and 0 <= j < n


def dijkstra(mapa, n):
    visitados =[[False] * n for _ in range(n)]
    bombas = [[float("inf")] * n for _ in range(n)]

    bombas[0][0] = mapa[0][0]

    fila = PriorityQueue()

    fila.put((mapa[0][0], 0, 0))

    while not fila.empty():
        #print(fila.queue)
        quantidade, i, j = fila.get()

        visitados[i][j] = True

        for di, dj in deslocamento:
            novoi = i + di
            novoj = j + dj
            if possivel(novoi, novoj, n):
                if not visitados[novoi][novoj] and bombas[novoi][novoj] > quantidade + mapa[novoi][novoj]:
                    bombas[novoi][novoj]= quantidade + mapa[novoi][novoj]
                    fila.put((quantidade + mapa[novoi][novoj], novoi, novoj))

    return bombas[n - 1][n -1]


def main():
    n = int(input())
    mapa = [[int(x) for x in input().split()] for _ in range(n)]

    result = dijkstra(mapa, n)

    print(result)

main()
from queue import PriorityQueue

def dijkstra(pontes, n):
    visitados = [False] * (n + 2)
    buracos = [float("inf")] * (n + 2)

    pq = PriorityQueue()

    pq.put((0, 0))

    while not pq.empty():
        qtd_atual, ponte_atual = pq.get()

        visitados[ponte_atual] = True

        for qtd_vizinho, ponte_vizinha in pontes[ponte_atual]:
            if not visitados[ponte_vizinha] and buracos[ponte_vizinha] > qtd_atual + qtd_vizinho:
                pq.put((qtd_atual + qtd_vizinho, ponte_vizinha))
                buracos[ponte_vizinha] = qtd_atual + qtd_vizinho

    return buracos[n + 1]


def main():
    n, m = [int(x) for x in input().split()]

    pontes = [[] for _ in range(n + 2)]

    for _ in range(m - 1):
        s, b, t = [int(x) for x in input().split()]
        pontes[s].append((t, b))
        pontes[b].append((t, s))

    result = dijkstra(pontes, n)

    print(result)


if __name__ == '__main__':
    main()
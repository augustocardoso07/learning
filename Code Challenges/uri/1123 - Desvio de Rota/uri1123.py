# -*- coding: utf-8 -*-
from queue import PriorityQueue


def na_rota(v, c):
    """ verifica se uma cidade v pertence a rota de 0 até c - 1"""
    return 0 <= v < c


def dijkstra(cidades, n, c, k):
    """ custo do menor caminho de k até c - 1"""
    distancias = [float("inf")] * n
    visitados = [False] * n
    distancias[k] = 0

    fila = PriorityQueue()

    fila.put((0, k))

    while not fila.empty():
        dist_atual, cidade_atual = fila.get()

        visitados[cidade_atual] = True

        for dist_vizinho, cidade_vizinha in cidades[cidade_atual]:
            nova_distancia = dist_atual + dist_vizinho
            if not visitados[cidade_vizinha] and nova_distancia < distancias[cidade_vizinha]:
                fila.put((nova_distancia, cidade_vizinha))
                distancias[cidade_vizinha] = nova_distancia

    return distancias[c - 1]


def main():
    while True:
        n, m, c, k = [int(x) for x in input().split()]
        if 0 == n == m == c == k: break

        cidades = [[] for _ in range(n)]

        for _ in range(m):
            u, v, p = [int(x) for x in input().split()]

            # so adiciona as duas estradas se
            # 1) as duas cidades estiverem fora da rota ou
            # 2) se as duas cidades forem consecutivas
            if (not na_rota(v, c) and not na_rota(u, c)) or (na_rota(v,c) and na_rota(u, c) and abs(v - u) == 1):
                cidades[u].append((p, v))
                cidades[v].append((p, u))

            # se somente v estiver na rota, so adiciona a estrada que chega em v
            if na_rota(v, c) and not na_rota(u, c):
                cidades[u].append((p, v))

            # se somente u estiver na rota, so adiciona a estrada que chega em u
            if not na_rota(v, c) and na_rota(u, c):
                cidades[v].append((p, u))

        result = dijkstra(cidades, n, c, k)
        print(result)

if __name__ == '__main__':
    main()
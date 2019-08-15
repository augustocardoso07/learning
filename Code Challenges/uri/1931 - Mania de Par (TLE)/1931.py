import sys
input = sys.stdin.readline

from queue import PriorityQueue


def somentepares(cidades, c):
    nova = [[] for _ in range(c)]

    for cidade in range(c):
        for custo1, vizinho in cidades[cidade]:
            for custo2, final in cidades[vizinho]:
                nova[cidade].append((custo1 + custo2, final))
                nova[final].append((custo1 + custo2, cidade))
    return nova


def dijkstra(cidades, c):
    visitados = [False] * c
    custos = [float("inf")] * c

    pq = PriorityQueue()

    pq.put((0, 0))

    while not pq.empty():
        custo_atual, cidade_atual = pq.get()
        if visitados[cidade_atual]: continue
        visitados[cidade_atual] = True

        for custo_vizinho, cidade_vizinha in cidades[cidade_atual]:
            if not visitados[cidade_vizinha] and custos[cidade_vizinha] > custo_atual + custo_vizinho:
                novocusto = custo_atual + custo_vizinho
                pq.put((novocusto, cidade_vizinha))
                custos[cidade_vizinha] = novocusto

    return -1 if custos[c-1] == float("inf") else custos[c-1]


def main():
    c, v = [int(x) for x in input().split()]

    cidades = [[] for _ in range(c)]
    for _ in range(v):
        v, u, g = [int(x) - 1 for x in input().split()]
        cidades[v].append((g + 1, u))
        cidades[u].append((g + 1, v))

    ncidades = somentepares(cidades, c)

    print(dijkstra(ncidades, c))


if __name__ == '__main__':
    main()


def test_all(capsys):
    import glob, sys
    ins = sorted(glob.glob("in*"))
    outs = sorted(glob.glob("out*"))

    assert len(ins) == len(outs)

    for i in range(len(ins)):
        pathin = ins[i]
        pathout = outs[i]

        sys.stdin = open(pathin)
        main()
        out, err = capsys.readouterr()
        exepeted = open(pathout).read()
        assert exepeted == out
        with capsys.disabled():
            print("\nTeste {} ===>: {} = {}".format(i, ins[i], outs[i]))

    sys.stdin = sys.__stdin__


def test_time(capsys):
    import sys
    pathin = "teste1"
    pathout = "saidateste1"
    sys.stdin = open(pathin)
    main()
    out, err = capsys.readouterr()
    exepeted = open(pathout).read()
    assert exepeted == out
def readinput():
    n = int(input()) + 1

    pecas = [[] for _ in range(n)]

    for _ in range(n - 1):
        i, j = [int(x) for x in input().split()]
        pecas[j].append(i)

    pecas_e_nivel = []

    vizinhos = [(0, 0, False)]
    visitado = [False] * n
    visitado[0] = True

    while len(vizinhos) != 0:
        peca, nivel, eh_folha = vizinhos.pop()

        if len(pecas[peca]) == 0:
            pecas_e_nivel.append((peca, nivel, True))
        else:
            pecas_e_nivel.append((peca, nivel, False))

            for u in pecas[peca]:
                if not visitado[u]:
                    visitado[u] = True
                    vizinhos.append((u, nivel + 1, 0))

    pecas_e_nivel.sort(reverse=True, key=lambda x: x[1])

    return pecas_e_nivel, pecas




def solve(pecas_e_nivel, pecas):
    d = dict()
    for peca, nivel, eh_folha in pecas_e_nivel:
        if eh_folha:
            d[peca] = 1
        else:
            soma = 1
            primeiro = d[pecas[peca][0]]
            for sub in pecas[peca]:
                soma += d[sub]
                if primeiro != d[sub]:
                    return False
            d[peca] = soma
    return True

def main():
    pecas_e_nivel, pecas = readinput()
    print("bem") if solve(pecas_e_nivel, pecas) else print("mal")


if __name__ == '__main__':
    main()

def test_all(capsys):
    import sys

    for i in range(1, 6):
        pathin = "in{}".format(i)
        pathout = "out{}".format(i)
        sys.stdin = open(pathin)
        main()
        result, err = capsys.readouterr()
        expected = open(pathout).read()
        assert result == expected
    sys.stdin = sys.__stdin__
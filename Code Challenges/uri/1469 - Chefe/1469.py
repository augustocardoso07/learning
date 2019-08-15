# -*- coding: utf-8 -*-
def idade_mimr(chefes, idades, vizinhos, result, visitados):
    if len(vizinhos) == 0: return result

    v = vizinhos.pop()
    visitados.add(v)
    novos_vizinhos = vizinhos + [u for u in chefes[v] if u not in visitados]

    return idade_mimr(chefes, idades, novos_vizinhos, min(idades[v], result), visitados)


def idade_mim(v, chefes, idades, n):
    if len(chefes[v]) == 0: return "*"

    idade = 101
    vizinhos = chefes[v].copy()
    visitados = [False] * n

    for u in vizinhos:
        visitados[u] = True

    while len(vizinhos) != 0:
        u = vizinhos.pop()

        if idades[u] < idade: idade = idades[u]

        for superior in chefes[u]:
            if not visitados[superior]:
                vizinhos.append(superior)
                visitados[u] = True

    return idade


def swap(chefes, a, b):
    chefes[a], chefes[b] = chefes[b], chefes[a]

    for superiores in chefes:
        for ii, v in enumerate(superiores):
            if v == a:
                superiores[ii] = b
            elif v == b:
                superiores[ii] = a


def main():
    while True:
        try:
            n, m, i = [int(x) for x in input().split()]
        except EOFError:
            break
        idades = [int(x) for x in input().split()]

        chefes = [[] for _ in range(n)]

        for _ in range(m):
            v, u = [int(x) - 1 for x in input().split()]
            chefes[u].append(v)

        for _ in range(i):
            op, *rest = input().split()
            if op == "T":
                a, b = [int(x) - 1 for x in rest]
                swap(chefes, a, b)
            else:
                v = int(rest[0]) - 1
                result = idade_mim(v, chefes, idades, n)
                print(result)


if __name__ == '__main__':
    main()


def test_all(capsys):
    import sys, time

    inicio = time.time()

    for i in range(1, 29):
        parcial = time.time()
        pathin = "input\\C_{}".format(i)
        pathout = "output\\C_{}".format(i)
        sys.stdin = open(pathin)
        main()
        result, err = capsys.readouterr()
        expected = open(pathout).read()
        assert result == expected
        with capsys.disabled():
            print("Teste {} == {}".format(i, time.time() - parcial))




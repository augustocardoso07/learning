# -*- coding: utf-8 -*-
from queue import Queue
DESLOCAMENTO = (
    ( 0, -1),
    ( 0,  1),
    ( 1,  0),
    (-1,  0),
    ( 1,  1),
    ( 1, -1),
    (-1,  1),
    (-1, -1)
)


def possivel(i, j, linhas, colunas):
    return 0 <= i < linhas and 0 <= j < colunas


def solve(a, b, m, linhas, colunas):
    total_dias = 1
    vizinhos = Queue()
    vizinhos.put((a, b, 0))
    m[a][b] = "."
    while not vizinhos.empty():
        i, j, dias = vizinhos.get()
        if dias > total_dias: total_dias = dias
        for di, dj in DESLOCAMENTO:
            novoi = i + di
            novoj = j + dj
            if possivel(novoi, novoj, linhas, colunas) and m[novoi][novoj] == 1:
                vizinhos.put((novoi, novoj, dias + 1))
                m[novoi][novoj] = "."
    return total_dias


def main():
    for _ in range(int(input())):
        linhas, colunas = [int(x) for x in input().split()]
        m = [[int(x) for x in input().split()] for _ in range(linhas)]
        a, b = [int(x) - 1 for x in input().split()]
        result = solve(a, b, m, linhas, colunas)
        print(result)


if __name__ == "__main__":
    main()


def test_all(capsys):
    import sys
    for i in range(1, 4):
        pathin = "in{}".format(i)
        pathout = "out{}".format(i)
        sys.stdin = open(pathin)
        main()
        out, err = capsys.readouterr()
        expected = open(pathout).read()
        assert out == expected
    sys.stdin = sys.__stdin__


def test_3(capsys):
    import sys
    pathin = "in3"
    pathout = "out3"
    sys.stdin = open(pathin)
    main()
    out, err = capsys.readouterr()
    expected = open(pathout).read()
    sys.stdin = sys.__stdin__
    assert out == expected
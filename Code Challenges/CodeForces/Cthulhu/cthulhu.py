import sys


def todos_visitados(list):
    return len(list) == sum(list)


def um_componente(vertices, n):
    vizinhos = [0]
    visitado = [False] * n

    while len(vizinhos) != 0:
        v = vizinhos.pop()
        visitado[v] = True

        for u in vertices[v]:
            if not visitado[u]:
                vizinhos.append(u)

    return todos_visitados(visitado)


def main():
    n, m = [int(x) for x in input().split()]

    vertices = [[] for _ in range(n)]

    for _ in range(m):
        v, u = [int(x) - 1 for x in input().split()]
        vertices[v].append(u)
        vertices[u].append(v)

    somente_um_ciclo = n == m and um_componente(vertices, n)

    print("FHTAGN!") if somente_um_ciclo else print("NO")

if __name__ == '__main__':
    main()

def testin1(capsys):
    sys.stdin = open("in1")
    main()
    out, err = capsys.readouterr()
    sys.stin = sys.__stdin__
    expected = open("in1_expeted").read()
    assert out == expected

def testin2(capsys):
    sys.stdin = open("in2")
    main()
    out, err = capsys.readouterr()
    sys.stin = sys.__stdin__
    expected = open("in2_expeted").read()
    assert out == expected

def testin3(capsys):
    sys.stdin = open("in3")
    main()
    out, err = capsys.readouterr()
    sys.stin = sys.__stdin__
    expected = open("in3_expeted").read()
    assert out == expected

def testin4(capsys):
    sys.stdin = open("in4")
    main()
    out, err = capsys.readouterr()
    sys.stin = sys.__stdin__
    expected = open("in4_expeted").read()
    assert out == expected

def testin5(capsys):
    sys.stdin = open("in5")
    main()
    out, err = capsys.readouterr()
    sys.stin = sys.__stdin__
    expected = open("in5_expeted").read()
    assert out == expected

def testin6(capsys):
    sys.stdin = open("in6")
    main()
    out, err = capsys.readouterr()
    sys.stin = sys.__stdin__
    expected = open("in6_expeted").read()
    assert out == expected

#https://stackoverflow.com/questions/26561822/pytest-capsys-checking-output-and-getting-it-reported
#https://stackoverflow.com/questions/35851323/pytest-how-to-test-a-function-with-input-call
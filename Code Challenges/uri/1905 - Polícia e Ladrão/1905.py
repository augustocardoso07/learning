deslocamento = (
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
)


def possible(i, j):
    return 0 <= i < 5 and 0 <= j < 5


def conect(mapa):
    vizinhos = [(0, 0)]

    if mapa[0][0] == "1": return False
    while len(vizinhos) != 0:
        i, j = vizinhos.pop()
        if (i, j) == (4, 4): return True
        mapa[i][j] = "!"

        for di, dj in deslocamento:
            novo_i = i + di
            novo_j = j + dj
            if possible(novo_i, novo_j) and mapa[novo_i][novo_j] == "0":
                vizinhos.append((novo_i, novo_j))

    return False


def input_mapa():
    k = 0
    m = []
    while k < 5:
        linha = input().split()

        if linha:
            m.append(linha)
            k += 1
    return m

n = int(input())

for _ in range(n):
    mapa = input_mapa()
    result = "COPS" if conect(mapa) else "ROBBERS"
    print(result)
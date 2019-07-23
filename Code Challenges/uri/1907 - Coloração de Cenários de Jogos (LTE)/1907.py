n, m = [int(x) for x in input().split()]

mapa = [[s for s in input()] for _ in range(n)]

deslocamento = (
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
)


def posivel(i, j):
    return 0 <= i < n and 0 <= j < m

def dfs(i, j):
    vizinhos = [(i, j)]

    while len(vizinhos) != 0:
        i, j = vizinhos.pop()
        mapa[i][j] = 'o'

        for di, dj in deslocamento:
            novo_i = i + di
            novo_j = j + dj
            if posivel(novo_i, novo_j) and mapa[novo_i][novo_j] == '.':
                vizinhos.append((novo_i, novo_j))


cout = 0

for i in range(n):
    for j in range(m):
        if mapa[i][j] == '.':
            dfs(i, j)
            cout += 1
print(cout)
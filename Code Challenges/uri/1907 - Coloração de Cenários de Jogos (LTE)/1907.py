from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]

mapa = [[s for s in input()] for _ in range(n)]

deslocamento = (
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
)


def possivel(i, j):
    return 0 <= i < n and 0 <= j < m

def dfs(i, j):
    vizinhos = [(i, j)]
    mapa[i][j] = 'o'

    while len(vizinhos) != 0:
        i, j = vizinhos.pop()

        for di, dj in deslocamento:
            novo_i = i + di
            novo_j = j + dj
            if possivel(novo_i, novo_j) and mapa[novo_i][novo_j] == '.':
                vizinhos.append((novo_i, novo_j))
                mapa[novo_i][novo_j] = 'o'

def dfsr(i, j):
    mapa[i][j] = "o"
    for di, dj in deslocamento:
        novoi = i + di
        novoj = j + dj
        if possivel(novoi, novoj) and mapa[novoi][novoj] == ".":
            dfsr(novoi, novoj)


count = 0


import time

a = time.time()
for i in range(n):
    for j in range(m):
        if mapa[i][j] == '.':
            dfsr(i, j)
            count += 1
print(count)
print(time.time() - a)
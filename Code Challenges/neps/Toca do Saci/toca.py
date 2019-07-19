n, m = [int(x) for x in input().split()]

mapa = []
for i in range(n):
    linha = input().split()
    mapa.append(linha)
    for j in range(m):
        if linha[j] == '3':
            start = (i, j)

deslocamento = (
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
)


def possible(i, j):
    return 0 <= i < n and 0 <= j < m


def dfs(start):
    result = 0
    vizinhos = [start]

    while len(vizinhos) != 0:
        i, j = vizinhos.pop()
        result += 1
        if mapa[i][j] == '2': return result
        mapa[i][j] = '!'
        for di, dj in deslocamento:
            novo_i = i + di
            novo_j = j + dj
            if possible(novo_i, novo_j) and (mapa[novo_i][novo_j] == '1' or mapa[novo_i][novo_j] == '2'):
                vizinhos.append((novo_i, novo_j))

result = dfs(start)
print(result)
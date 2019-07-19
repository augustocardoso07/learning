m, n = [int(x) for x in input().split()]
mapa = [input() for _ in range(m)]

deslocamento = [
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1)
]

def na_borda(i, j):
    return i == 0 or j == 0 or i == (m - 1) or j == (n - 1)

def do_lado_dagua(i, j):
    return mapa[i][j] == '.'

def eh_costa(i, j):
    if na_borda(i, j): return True
    for ii, jj in deslocamento:
        novo_i = i + ii
        novo_j = j + jj
        if do_lado_dagua(novo_i, novo_j):
            return True
    return False

result = 0
for i in range(m):
    for j in range(n):
        if mapa[i][j] == '.': continue
        if eh_costa(i, j): result += 1

print(result)
DESLOCAMENTO = (
    (-1,  0), # pra cima
    ( 1,  0), # pra baixo
    ( 0, -1), # pra esquerda
    ( 0,  1)  # par direita
)


def possivel(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def site_vazio(maze, n, m):
    for i in range(n):
        for j in range(m):
            if maze[i][j] == ".":
                return i, j

def dfs(maze, n, m, limite):
    visitados = [[False] * m for _ in range(n)]

    i, j = site_vazio(maze, n, m)

    vizinhos = [(i, j)]
    count = 0
    while len(vizinhos) != 0:
        i, j = vizinhos.pop()
        visitados[i][j] = True
        count += 1
        if count > limite: maze[i][j] = "X"
        for di, dj in DESLOCAMENTO:
            novoi = i + di
            novoj = j + dj
            if possivel(novoi, novoj, n, m) and not visitados[novoi][novoj] and maze[novoi][novoj] == ".":
                vizinhos.append((novoi, novoj))
                visitados[novoi][novoj] = True



n, m, k = [int(x) for x in input().split()]

maze = [[s for s in input()] for _ in range(n)]

total_livre = sum(linha.count(".") for linha in maze)

dfs(maze, n, m, total_livre - k)

for linha in maze:
    print(*linha, sep="")
n = int(input())
for i in range(4, n + 4):
    tamanho = int(input())
    m = [[int(x) ** 2 for x in input().split()] for _ in range(tamanho)]
    mt = [[m[j][i] for j in range(tamanho)] for i in range(tamanho)]
    max_by_collum = [len(str(max(linha))) for linha in mt]
    print("Quadrado da matriz #{}:".format(i)) if i == 4 else print("\nQuadrado da matriz #{}:".format(i))
    for i in range(tamanho):
        linha = ""
        for j in range(tamanho):
            linha += "{:>{}} ".format(m[i][j], max_by_collum[j])
        print(linha.rstrip())

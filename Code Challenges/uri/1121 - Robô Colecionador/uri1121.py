PILASTRA = "#"
NORMAL = "."
FIGURA = "*"
DESLOCAMENTO = {
    "N": (-1,  0),
    "S": ( 1,  0),
    "L": ( 0,  1),
    "O": ( 0, -1)
}


def girar(direcao, face):
    if direcao == "D":
        if face == "N": return "L"
        if face == "L": return "S"
        if face == "S": return "O"
        if face == "O": return "N"
    else:
        if face == "N": return "O"
        if face == "O": return "S"
        if face == "S": return "L"
        if face == "L": return "N"


def possible(x, y, n, m, mapa):
    return 0 <= x < n and 0 <= y < m and mapa[x][y] != PILASTRA


def solve(n, m, s, mapa, instrucoes, x, y, face):
    result = 0
    for ins in instrucoes:
        if ins == "F":
            dx, dy = DESLOCAMENTO[face]
            if possible(dx + x, dy + y, n, m, mapa):
                x, y = dx + x, dy + y
        else:
            face = girar(ins, face)
        if mapa[x][y] == FIGURA:
            result += 1
            mapa[x][y] = "."

    return result


def main():
    while True:
        n, m, s = [int(x) for x in input().split()]
        if 0 == n == m == s: break
        mapa = []
        faces = {"N", "S", "L", "O"}
        for i in range(n):
            linha = []
            strlinhs = input()
            for j in range(m):
                if strlinhs[j] in faces:
                    x, y = i, j
                    face = strlinhs[j]
                    linha.append(".")
                else:
                    linha.append(strlinhs[j])
            mapa.append(linha)
        instrucoes = input()
        result = solve(n, m, s, mapa, instrucoes, x, y, face)
        print(result)


if __name__ == '__main__':
    main()
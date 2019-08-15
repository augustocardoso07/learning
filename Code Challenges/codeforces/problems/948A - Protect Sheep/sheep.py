deslocamento = (
    ( 0, -1),
    ( 0,  1),
    ( 1,  0),
    (-1,  0)
)


def possivel(novoi, novoj, r, c):
    return 0 <= novoi < r and 0 <= novoj < c


def solve(mapa, r, c):
    for i in range(r):
        for j in range(c):
            if mapa[i][j] == "W":
                for di, dj in deslocamento:
                    novoi = i + di
                    novoj = j + dj
                    if possivel(novoi, novoj, r, c):
                        if mapa[novoi][novoj] == "S":
                            return False
                        elif mapa[novoi][novoj] == ".":
                            mapa[novoi][novoj] = "D"
    return True


def main():
    r, c = [int(x) for x in input().split()]

    mapa = [[s for s in input()] for _ in range(r)]

    possivel = solve(mapa, r, c)

    if possivel:
        print("Yes")
        for linha in mapa:
            print(*linha, sep="")
    else:
        print("No")

if __name__ == '__main__':
    main()
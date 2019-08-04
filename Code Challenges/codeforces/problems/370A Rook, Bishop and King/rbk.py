def nrook(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2: return 1
    return 2


def nking(r1, c1, r2, c2):
    dr = abs(r1 - r2)
    dc = abs(c1 - c2)
    return dr + dc - min(dr, dc)


def iswhite(r, c):
    return c % 2 != 0 if r % 2 else c % 2 == 0


def nbishop(r1, c1, r2, c2):
    if iswhite(r1, c1) != iswhite(r2, c2): return 0
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2: return 1
    return 2


def main():
    r1, c1, r2, c2 = [int(x) - 1 for x in input().split()]
    rook = nrook(r1, c1, r2, c2)
    bishop = nbishop(r1, c1, r2, c2)
    king = nking(r1, c1, r2, c2)
    print(rook, bishop, king)

if __name__ == '__main__':
    main()
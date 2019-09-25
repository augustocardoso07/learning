def solve(a, c, final):
    result = a - final[0]

    for i in range(c - 1):
        if final[i] > final[i + 1]:
            result += final[i] - final[i + 1]

    return result


def solve_slow(a, c, final):
    result = 0
    for altura in range(a, -1, -1):
        ligado = False
        for i in range(c):
            if final[i] < altura:
                if not ligado:
                    result += 1
                ligado = True
            else:
                ligado = False
    return result


def main():
    while True:
        a, c = [int(x) for x in input().split()]
        if 0 == a == c:
            break
        final = [int(x) for x in input().split()]
        result = solve(a, c, final)
        print(result)


if __name__ == '__main__':
    main()

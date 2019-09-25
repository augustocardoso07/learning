def solve(o, b, i):
    mi = min(o, b, i)
    if o == b or o == i or b == i:
        return "Empate"
    if mi == o:
        return "Otavio"
    if mi == b:
        return "Bruno"
    return "Ian"


def main():
    o, b, i = [float(x) for x in input().split()]
    result = solve(o, b, i)
    print(result)


if __name__ == '__main__':
    main()
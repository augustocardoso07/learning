def solve(a, b):
    mi = min(a, b)
    ma = str(max(a, b))

    result = 0
    for i in range(-1, -len(ma) - 1, -1 ):
        if int(mi[i]) + int(ma[i]) > 9: result += 1

    return result


def main():
    while True:
        a, b = [int(x) for x in input().split()]
        if 0 == a == b: break
        result = solve(a, b)
        if result == 0:
            print("No carry operation.")
        elif result == 1:
            print("1 carry operation.")
        else:
            print("{} carry operations.".format(result))


if __name__ == '__main__':
    main()
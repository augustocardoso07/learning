def solve(n, m):
    result = 0
    for i in range(n, m + 1):
        s = str(i)
        if len(set(s)) == len(s):
            result += 1
    return result


def main():
    while True:
        try:
            n, m = [int(x) for x in input().split()]
        except:
            break
        result = solve(n, m)
        print(result)


if __name__ == '__main__':
    main()
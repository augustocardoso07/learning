def main():
    t = int(input())
    for _ in range(t):
        c, d = [int(x) for x in input().split()]
        if c == d == 0:
            result = 0
        else:
            result = (26 ** c) * (10 ** d)
        print(result)


if __name__ == '__main__':
    main()
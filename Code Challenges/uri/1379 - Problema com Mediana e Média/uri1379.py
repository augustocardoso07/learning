def main():
    while True:
        b, c = [int(x) for x in input().split()]
        if 0 == b == c: break
        a = 2 * b - c
        print(a)


if __name__ == '__main__':
    main()
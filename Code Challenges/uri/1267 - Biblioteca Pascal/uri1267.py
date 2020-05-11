def main():
    while True:
        n, d = [int(x) for x in input().split()]
        if 0 == n == d: break
        jantares = [0] * n
        for _ in range(d):
            jantar = [int(x) for x in input().split()]
            for i in range(n):
                jantares[i] += jantar[i]

        if d in jantares:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()
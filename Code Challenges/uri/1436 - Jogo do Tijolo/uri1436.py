def main():
    t = int(input())
    for i in range(1, t + 1):
        n, *idades = [int(x) for x in input().split()]
        print("Case {}: {}".format(i, idades[int(n/2)]))


if __name__ == '__main__':
    main()
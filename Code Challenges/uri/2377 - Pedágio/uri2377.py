from math import floor


def main():
    l, d = [int(x) for x in input().split()]
    p, k = [int(x) for x in input().split()]
    print(l*p + floor(l/d) * k)


if __name__ == '__main__':
    main()
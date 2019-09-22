from math import log, ceil


def main():
    n = int(input())
    for _ in range(n):
        c = float(input())
        print("{} dias".format(ceil(log(c, 2))))


if __name__ == '__main__':
    main()
from math import pow


def main():
    while True:
        a, b, c = [int(x) for x in input().split()]
        if 0 == a == b == c: break
        volume = a * b * c
        print(int(pow(volume, 1/3)))


if __name__ == '__main__':
    main()
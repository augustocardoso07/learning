from math import factorial


def main():
    while True:
        try:
            m, n = [int(x) for x in input().split()]
        except EOFError:
            break
        print(factorial(m) + factorial(n))


if __name__ == '__main__':
    main()
def main():
    a, b = [int(x) for x in input().split()]
    result = (a + b) * (b - a + 1) / 2
    print(int(result))


if __name__ == '__main__':
    main()
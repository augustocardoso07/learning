def main():
    a, b, c, d = [int(x) for x in input().split()]
    if a * b == c * d:
        print(0)
    elif a * b > c * d:
        print(-1)
    else:
        print(1)


if __name__ == '__main__':
    main()

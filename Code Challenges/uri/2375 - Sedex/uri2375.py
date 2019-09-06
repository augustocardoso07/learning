def main():
    n = int(input())
    a, l, p = [int(x) for x in input().split()]
    if n <= a and n <= l and n <= p:
        print("S")
    else:
        print("N")


if __name__ == '__main__':
    main()
def main():
    n = int(input())
    la, lb = [int(x) for x in input().split()]
    sa, sb = [int(x) for x in input().split()]
    if la <= n <= lb and sa <= n <= sb:
        print("possivel")
    else:
        print("impossivel")


if __name__ == '__main__':
    main()
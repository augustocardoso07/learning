def main():
    a, g, ra, rg = [float(x) for x in input().split()]
    if ra / a > rg / g:
        print("A")
    else:
        print("G")


if __name__ == '__main__':
    main()
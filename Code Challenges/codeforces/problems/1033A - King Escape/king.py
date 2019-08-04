def q(ax, ay, x, y):
    if ax < x and ay < y: return 1
    if ax > x and ay < y: return 2
    if ax < x and ay > y: return 3
    if ax > x and ay > y: return 4
    return 0


def main():
    n = int(input())
    ax, ay = [int(x) for x in input().split()]
    bx, by = [int(x) for x in input().split()]
    cx, cy = [int(x) for x in input().split()]

    if q(ax, ay, bx, by) == q(ax, ay, cx, cy):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
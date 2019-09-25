def solve(n, grid, chegada):
    result = 0
    for i in range(n):
        j = grid.index(chegada[i])
        while grid[i] != chegada[i]:
            grid[j - 1], grid[j] = grid[j], grid[j - 1]
            j = j - 1
            result += 1
    return result


def main():
    while True:
        try:
            n = int(input())
            grid = [int(x) for x in input().split()]
            chegada = [int(x) for x in input().split()]
        except EOFError:
            break
        result = solve(n, grid, chegada)
        print(result)


if __name__ == '__main__':
    main()

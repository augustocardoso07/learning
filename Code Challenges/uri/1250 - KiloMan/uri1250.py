def solve(t, height, moves):
    result = 0
    for i in range(t):
        if moves[i] == "J" and height[i] > 2 or moves[i] == "S" and height[i] <= 2:
            result += 1
    return result


def main():
    n = int(input())
    for _ in range(n):
        t = int(input())
        height = [int(x) for x in input().split()]
        moves = [s for s in input()]
        result = solve(t, height, moves)
        print(result)


if __name__ == '__main__':
    main()
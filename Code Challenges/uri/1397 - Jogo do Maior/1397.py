def main():
    while True:
        n = int(input())
        if n == 0: break
        result_a, result_b = 0, 0
        for _ in range(n):
            a, b = [int(x) for x in input().split()]
            if a > b: result_a += 1
            if b > a: result_b += 1
        print(result_a, result_b)


if __name__ == '__main__':
    main()
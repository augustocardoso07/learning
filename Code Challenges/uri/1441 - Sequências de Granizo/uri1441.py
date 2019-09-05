def solve(n):
    result = 1
    while n != 1:
        if n > result: result = n
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return int(result)


def main():
    while True:
        n = int(input())
        if n == 0: break
        result = solve(n)
        print(result)


if __name__ == '__main__':
    main()


def test_uri1441():
    assert 16 == solve(5)
    assert 52 == solve(11)
    assert 9232 == solve(27)
    assert 1 == solve(1)
    assert 8 == solve(8)
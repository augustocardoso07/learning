def solve(a, b):
    if 0 <= b <= 2:
        return "nova"
    if 3 <= b <= 96:
        if a > b:
            return "minguante"
        else:
            return "crescente"
    if 97 <= b <= 100:
        return "cheia"



def main():
    a, b = [int(x) for x in input().split()]
    result = solve(a, b)
    print(result)

if __name__ == '__main__':
    main()


def test_one():
    assert "nova" == solve(0, 2)
    assert "crescente" == solve(2, 3)
    assert "cheia" == solve(99, 97)
    assert "minguante" == solve(97, 94)
    assert "crescente" == solve(30, 35)
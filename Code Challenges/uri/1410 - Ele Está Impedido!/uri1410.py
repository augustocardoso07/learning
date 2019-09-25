def solve(atacante, defensores):
    if atacante >= defensores[1] or (atacante == defensores[0] and atacante == defensores[1]):
        return "N"
    return "Y"


def main():
    while True:
        a, b = [int(x) for x in input().split()]
        if 0 == a == b: break
        atacantes = sorted([int(x) for x in input().split()])
        defensores = sorted([int(x) for x in input().split()])
        result = solve(atacantes[0], defensores)
        print(result)


if __name__ == '__main__':
    main()
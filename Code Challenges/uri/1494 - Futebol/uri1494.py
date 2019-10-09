def main():
    while True:
        try:
            n, g = [int(x) for x in input().split()]
        except EOFError:
            break

        result = 0
        perdas = []
        for _ in range(n):
            s, r = [int(x) for x in input().split()]
            if s > r:
                result += 3
            elif s == r:
                if g:
                    g -= 1
                    result += 3
                else:
                    result += 1
            else:
                perdas.append(r - s + 1)
        perdas.sort()

        for i in range(len(perdas)):
            if g <= 0: break
            p = perdas[i]
            if g - p >= 0:
                g -= p
                perdas[i] = 0
                result += 3
        if g and 2 in perdas:
            result += 1
        print(perdas)
        print(result)


if __name__ == '__main__':
    main()
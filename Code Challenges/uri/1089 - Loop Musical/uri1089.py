def main():
    while 1:
        n = int(input())
        if n == 0: break
        notas = [int(x) for x in input().split()]
        result = 0
        for i in range(n):
            anterior = notas[(i - 1) % n]
            atual = notas[i]
            proximo = notas[(i + 1) % n]
            if not (anterior < atual < proximo or anterior > atual > proximo):
                result += 1
        print(result)


if __name__ == '__main__':
    main()
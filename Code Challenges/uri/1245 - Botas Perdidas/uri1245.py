def main():
    while 1:
        try:
            n = int(input())
        except EOFError:
            break
        d = dict()
        for _ in range(n):
            tamanho, lado = input().split()
            contagem = d.get(tamanho, (0, 0))
            if lado == "E":
                d[tamanho] = (contagem[0] + 1, contagem[1])
            else:
                d[tamanho] = (contagem[0], contagem[1] + 1)

        result = 0
        for key, value in d.items():
            result += min(value[0], value[1])

        print(result)


if __name__ == '__main__':
    main()
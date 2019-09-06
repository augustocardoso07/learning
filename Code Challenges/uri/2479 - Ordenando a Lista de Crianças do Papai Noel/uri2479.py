def main():
    n = int(input())
    lista = []
    comportados = 0
    nao_comportados = 0
    for _ in range(n):
        sinal, nome = input().split()
        lista.append(nome)
        if sinal == "+":
            comportados += 1
        else:
            nao_comportados += 1
    lista.sort()
    print(*lista, sep="\n")
    print("Se comportaram: {} | Nao se comportaram: {}".format(comportados, nao_comportados))


if __name__ == '__main__':
    main()
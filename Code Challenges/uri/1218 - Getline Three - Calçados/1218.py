caso = 0

while True:
    try:
        calsado = input()
    except:
        break
    linha = input().split()
    caso += 1

    f = 0
    m = 0
    c = 0

    for i in range(len(linha)):
        info = linha[i]
        if info == calsado:
            c += 1
            if linha[i + 1] == "F": f += 1
            if linha[i + 1] == "M": m += 1

    print("Caso 1:") if caso == 1 else print("\nCaso {}:".format(caso))
    print("Pares Iguais: {}".format(c))
    print("F: {}".format(f))
    print("M: {}".format(m))
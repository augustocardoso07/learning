def main():
    n = int(input())
    suporte = float(input())
    confianca = float(input())

    palavras = []
    for _ in range(n):
        palavras.append(input())

    conjunto = set()
    freq = dict()

    for palavra in palavras:
        for letra in palavra:
            conjunto.add(letra)
            freq[letra] = freq.get(letra, 0) + 1

    lista = list(conjunto)
    result = []
    result2 = []

    for i in range(len(lista)):
        for j in range(i, len(lista)):
            letra1 = lista[i]
            letra2 = lista[j]
            if letra1 == letra2: continue
            nas_duas = 0
            somente_letra_1 = 0
            somente_letra_2 = 0
            for palavra in palavras:
                if letra1 in palavra:
                    somente_letra_1 += 1
                if letra2 in palavra:
                    somente_letra_2 += 1
                if letra1 in palavra and letra2 in palavra:
                    nas_duas += 1
            suporte_letras = nas_duas / n

            if suporte_letras >= suporte:
                confianca_letras = nas_duas / somente_letra_1
                confianca_letras2 = nas_duas / somente_letra_2

                if confianca_letras >= confianca:
                    result.append("{} -> {} [{:.3f} {:.3f}]".format(letra1, letra2, confianca_letras, suporte_letras))

                if confianca_letras2 >= confianca:
                    result2.append("{} -> {} [{:.3f} {:.3f}]".format(letra2, letra1, confianca_letras2, suporte_letras))


    result_fianl = sorted(result + result2)

    if result_fianl:
        print(*result_fianl, sep="\n")
    else:
        print("nada foi encontrado")



if __name__ == '__main__':
    main()
def read_info(meses, parcela, valor, vezes):
    return int(meses), float(parcela), float(valor), int(vezes)

def read_depr(mes, depr):
    return int(mes), float(depr)

def fill(list):
    depr = list[0]
    for i, value in enumerate(list):
        if value == 0:
            list[i] = depr
        else:
            depr = list[i]

while True:
    meses, parcela, valor, vezes = read_info(*input().split())
    if meses < 0:
        break

    valor += parcela
    valor_atual = valor

    depr_list = [0] * meses

    for _ in range(vezes):
        mes, depr = read_depr(*input().split())
        depr_list[mes] = depr

    fill(depr_list)

    for i, depr in enumerate(depr_list):
        valor_atual -= parcela
        valor *= (1 - depr)

        if valor > valor_atual:
            if i == 1:
                print("{} month".format(i))
            else:
                print("{} months".format(i))
            break
            #print(valor_atual)
            #print(valor)

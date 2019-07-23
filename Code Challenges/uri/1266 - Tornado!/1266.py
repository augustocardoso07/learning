while True:
    n = int(input())
    if n == 0: break
    cerca = [int(x) for x in input().split()]
    result = 0
    tamanho = len(cerca)

    if tamanho > 5:
        if cerca[-2] == cerca[-1] == cerca[0] == cerca[1] == cerca[2] == 0:
            cerca[-1] = 1
            result += 1

    for i in range(tamanho):
        atual = cerca[i]
        anterior = cerca[(i - 1) % tamanho]
        proximo = cerca[(i + 1) % tamanho]
        if atual == anterior == proximo == 0:
            result += 1
            cerca[i] = 1
            #print(cerca)
    for i in range(tamanho):
        atual = cerca[i]
        proximo = cerca[(i + 1) % tamanho]
        if atual == proximo == 0:
            cerca[i] = 1
            result += 1
    print(result)

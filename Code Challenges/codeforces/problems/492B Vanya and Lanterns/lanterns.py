n, l = [int(x) for x in input().split()]
lanternas = [int(x) for x in input().split()]
lanternas.sort()

pares_de_lanternas = []
pares_de_lanternas.append((-lanternas[0], lanternas[0]))

for i in range(1, n):
    anterior = lanternas[i - 1]
    atual = lanternas[i]
    pares_de_lanternas.append((anterior, atual))

pares_de_lanternas.append((lanternas[n - 1], lanternas[n - 1] + 2 * (l - lanternas[n - 1])))


def diferenca(item):
    return abs(item[1] - item[0])


par = max(pares_de_lanternas, key=diferenca)

print("{:.10f}".format(abs(par[1] - par[0]) / 2))
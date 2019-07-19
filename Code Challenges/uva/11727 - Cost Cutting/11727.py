n = int(input())
for i in range(1, n + 1):
    lista = [int(x) for x in input().split()]
    lista.sort()
    print("Case {}: {}".format(i, lista[1]))
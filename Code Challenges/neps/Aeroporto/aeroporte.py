count = 0
while True:
    a, v = [int(x) for x in input().split()]
    if a == v == 0: break
    d = {}
    for _ in range(v):
        x, y = [int(x) for x in input().split()]
        d[x] = d.get(x, 0) + 1
        d[y] = d.get(y, 0) + 1
    lista = list(d.items())
    maoir = max(lista, key=lambda x: x[1])
    result = [item[0] for item in lista if item[1] == maoir[1]]
    result.sort()
    count += 1
    if count == 1:
        print("Teste", count)
    else:
        print("\nTeste", count)
    print(*result)
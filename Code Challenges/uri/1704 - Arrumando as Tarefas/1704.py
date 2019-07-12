while True:
    try:
        n, h = [int(x) for x in input().split()]
    except EOFError:
        break
    lista = []
    for _ in range(n):
        lista.append([int(x) for x in input().split()])
    lista.sort(reverse=True)
    #print(lista)
    result = sum([item[0] for item in lista[h:]])
    print(result)
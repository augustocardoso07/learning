for t in range(int(input())):
    conjunto = []
    for n in range(int(input())):
        conjunto.append(set(input().split()[1:]))

    for q in range(int(input())):
        op, a, b = [int(x) - 1 for x in input().split()]
        if op == 0:
            resultado = conjunto[a] & conjunto[b]
        elif op == 1:
            resultado = conjunto[a] | conjunto[b]
        print(len(resultado))

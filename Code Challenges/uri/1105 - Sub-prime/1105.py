while True:
    b, n = [int(x) for x in input().split()]
    if b == n == 0: break
    saldo = [int(x) for x in input().split()]
    for _ in range(n):
        a, b, valor = [int(x) for x in input().split()]
        saldo[a - 1] -= valor
        saldo[b - 1] += valor

    possivel = True

    for v in saldo:
        if v < 0:
            possivel = False
            break
    print("S") if possivel else print("N")
def solve(inicio, k, l):
    while len(l) != 1:
        indice_do_removido = (inicio + k) % len(l)
        l.pop(indice_do_removido)
        indice_do_anterior = indice_do_removido - 1
        inicio = indice_do_anterior
    return l[0]


def main():
    nc = int(input())
    for i in range(1, nc + 1):
        n, k = [int(x) for x in input().split()]
        result = solve(-1, k, list(range(1, n + 1)))
        print("Case {}: {}".format(i, result))


if __name__ == '__main__':
    main()
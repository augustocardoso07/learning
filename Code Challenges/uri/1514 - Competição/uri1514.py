def main():
    while True:
        n, m = [int(x) for x in input().split()]
        if 0 == n == m: break
        criterio1 = True
        criterio2 = True
        criterio3 = True
        criterio4 = True
        problemas = [0] * m
        for _ in range(n):
            competidor = [int(x) for x in input().split()]
            if sum(competidor) == m: criterio1 = False
            if sum(competidor) == 0: criterio4 = False

            for i in range(len(competidor)):
                if competidor[i]: problemas[i] += 1

        if 0 in problemas: criterio2 = False

        for n_de_resolvidos in problemas:
            if n_de_resolvidos == n:
                criterio3 = False

        print(criterio1 + criterio2 + criterio3 + criterio4)


if __name__ == '__main__':
    main()
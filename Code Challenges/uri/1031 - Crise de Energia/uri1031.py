def find_m(lista, salto):
    inicio = -salto
    while lista:
        to_remove = (inicio + salto) % len(lista)
        out = lista.pop(to_remove)
        #print(lista)
        #print(out)
        if out == 13:
            if len(lista) == 0:
                return True
            else:
                return False
        inicio = to_remove - 1


def solve(n):
    for salto in range(1, 240):
        lista = list(range(1, n + 1))
        found = find_m(lista, salto)
        if found:
            return salto


def main():
    while True:
        n = int(input())
        if n == 0: break
        result = solve(n)
        print(result)


if __name__ == '__main__':
    #find_m(list(range(1, 18)), 5)
    main()
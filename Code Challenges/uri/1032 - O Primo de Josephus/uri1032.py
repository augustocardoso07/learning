from math import floor, sqrt


def primo_7(n):
   if n % 2 == 0: return n == 2
   divisor = 3
   raiz = floor(sqrt(n))
   while divisor <= raiz and n % divisor != 0: divisor += 2
   return n > 1 and divisor > raiz


primos = [x for x in range(100000) if primo_7(x)]


def josephus_prime(inicio, l):
    m = 0
    while len(l) != 1:
        indice_do_removido = (inicio + primos[m]) % len(l)
        l.pop(indice_do_removido)
        inicio = indice_do_removido - 1
        m += 1
    return l[0]


def main():
    while True:
        n = int(input())
        if n == 0: break
        result = josephus_prime(-1, list(range(1, n + 1)))
        print(result)


if __name__ == '__main__':
    main()
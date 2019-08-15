# Uses python3
import sys, math
from math import sqrt, pow


def fibo(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)

    return current

def period_len(m):
    previous = 0
    current  = 1
    c = 0
    while True:
        c += 1
        previous, current = current % m, (previous + current) % m
        if previous == 0 and current == 1:
            break

    return c


def get_fibonacci_huge(n, m):
    x = period_len(m)
    remainder = n % x
    return fibo(remainder) % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

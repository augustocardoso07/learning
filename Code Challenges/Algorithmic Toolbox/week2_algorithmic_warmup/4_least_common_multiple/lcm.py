# Uses python3
import sys

# Much more effective way to get the least common multiple of two numbers is to multiply them and divide
# the result by their greatest common divisor. The greatest common divisor may be computed by the Euclidean
# algorithm, which is very fast, because it does not require factorization of the given numbers.
# http://www.programming-algorithms.net/article/42865/Least-common-multiple


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def lcm(a, b):
    return int((a*b) / gcd(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))


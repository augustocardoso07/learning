from math import floor, sqrt


def primo_7(n):
   if n % 2 == 0: return n == 2
   divisor = 3
   raiz = floor(sqrt(n))
   while divisor <= raiz and n % divisor != 0: divisor += 2
   return n > 1 and divisor > raiz


def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        if primo_7(x):
            print("Prime")
        else:
            print("Not Prime")


if __name__ == '__main__':
    main()
from sys import stdin, stdout
input = stdin.readline

#Counting sort
def solve(alturas, tamanho):
    tamanhos = [0] * 231

    for altura in alturas:
        tamanhos[altura] += 1

    result = []

    for i in range(20, 231):
        for j in range(tamanhos[i]):
            result.append(i)

    return result


def main():
    n = int(input())
    for _ in range(n):
        tamanho = int(input())
        alturas = [int(x) for x in input().split()]
        result = solve(alturas, tamanho)
        stdout.write(" ".join(map(str, result)) + "\n")


if __name__ == '__main__':
    main()


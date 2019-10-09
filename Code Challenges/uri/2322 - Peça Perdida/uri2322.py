def main():
    n = int(input())
    numeros = {int(x) for x in input().split()}
    for result in numeros.symmetric_difference(set(range(1, n + 1))):
        print(result)


if __name__ == '__main__':
    main()

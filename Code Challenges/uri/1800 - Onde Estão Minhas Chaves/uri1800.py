def main():
    q, e = [int(x) for x in input().split()]
    visitados = {int(x) for x in input().split()}
    for _ in range(q):
        escritorio = int(input())
        if escritorio in visitados:
            print(0)
        else:
            print(1)
            visitados.add(escritorio)


if __name__ == '__main__':
    main()
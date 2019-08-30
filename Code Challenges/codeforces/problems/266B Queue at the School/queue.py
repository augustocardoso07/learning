def main():
    n, t = [int(x) for x in input().split()]
    fila = [letra for letra in input()]

    for time in range(t):
        for i in range(len(fila) - 1):
            if fila[i] == "B" and fila[i + 1] == "G":
                fila[i], fila[i + 1] = fila[i + 1], fila[i]

    print("".join(fila))

if __name__ == '__main__':
    main()
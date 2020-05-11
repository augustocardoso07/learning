def main():
    consumo = int(input())
    if consumo <= 10:
        result = 7
    elif consumo <= 30:
        result = 7 + (consumo - 10)
    elif consumo <= 100:
        result = 27 + (consumo - 30) * 2
    else:
        result = 167 + (consumo - 100) * 5
    print(result)


if __name__ == '__main__':
    main()
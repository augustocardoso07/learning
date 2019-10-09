def solve(digitos):
    soma1 = 0
    soma2 = 0
    for i in range(9):
        a = int(digitos[i])
        soma1 += (a * (i + 1))
        soma2 += (a * (9 - i))

    digito1 = (soma1 % 11) % 10
    digito2 = (soma2 % 11) % 10

    return "{}.{}.{}-{}{}".format(digitos[:3], digitos[3:6], digitos[6:], digito1, digito2)


def main():
    while True:
        try:
            cpfstr = input()
        except EOFError:
            break
        result = solve(cpfstr)
        print(result)


if __name__ == '__main__':
    main()
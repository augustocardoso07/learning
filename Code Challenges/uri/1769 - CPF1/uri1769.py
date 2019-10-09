def solve(digitos, verificador):
    soma1 = 0
    soma2 = 0
    for i in range(9):
        a = int(digitos[i])
        soma1 += (a * (i + 1))
        soma2 += (a * (9 - i))

    digito1 = (soma1 % 11) % 10
    digito2 = (soma2 % 11) % 10

    if digito1 == int(verificador[0]) and digito2 == int(verificador[1]):
        return "CPF valido"
    return "CPF invalido"


def main():
    while True:
        try:
            cpfstr = input()
        except EOFError:
            break
        precpf, verificador = cpfstr.split("-")
        result = solve(precpf.replace(".", ""), verificador)
        print(result)


if __name__ == '__main__':
    main()
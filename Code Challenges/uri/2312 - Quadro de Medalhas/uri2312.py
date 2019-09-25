class Pais:
    def __init__(self, nome, ouro, prata, bronze):
        self.nome = nome
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze

    def __str__(self):
        return "{} {} {} {}".format(self.nome, self.ouro, self.prata, self.bronze)


def ordena(pais):
    return pais.ouro, pais.prata, pais.bronze


def main():
    n = int(input())
    lista = []
    for _ in range(n):
        nome, ouro, prata, bronze = input().split()
        lista.append(Pais(nome, int(ouro), int(prata), int(bronze)))
    lista.sort(key=lambda pais: pais.nome)
    lista.sort(key=ordena, reverse=True)

    for pais in lista:
        print(pais)


if __name__ == '__main__':
    main()
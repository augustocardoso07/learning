def solve(aposta, sorteio):
    size = len(aposta.intersection(sorteio))
    if size == 3:
        return "terno"
    if size == 4:
        return "quadra"
    if size == 5:
        return "quina"
    if size == 6:
        return "sena"
    return "azar"


def main():
    aposta = {x for x in input().split()}
    sorteio = {x for x in input().split()}
    result = solve(aposta, sorteio)
    print(result)


if __name__ == '__main__':
    main()
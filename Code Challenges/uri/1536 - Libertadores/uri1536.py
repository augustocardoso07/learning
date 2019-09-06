def resultado(time1, time2):
    if time1 > time2:
        return 3, 0
    if time2 > time1:
        return 0, 3
    return 1, 1


def pontos(time1jogo1, time2jogo1, time2jogo2, time1jogo2):
    parcial11, parcial21 = resultado(time1jogo1, time2jogo1)
    parcial12, parcial22 = resultado(time1jogo2, time2jogo2)
    return parcial11 + parcial12, parcial21 + parcial22


def solve(time1jogo1, time2jogo1, time2jogo2, time1jogo2):
    pontos1, pontos2 = pontos(time1jogo1, time2jogo1, time2jogo2, time1jogo2)
    saldo1 = time1jogo1 + time1jogo2
    saldo2 = time2jogo1 + time2jogo2
    gols_na_casa_asversario1 = time1jogo2
    gols_na_casa_asversario2 = time2jogo1
    if pontos1 > pontos2:
        return "Time 1"
    if pontos2 > pontos1:
        return "Time 2"
    if saldo1 > saldo2:
        return "Time 1"
    if saldo2 > saldo1:
        return "Time 2"
    if gols_na_casa_asversario1 > gols_na_casa_asversario2:
        return "Time 1"
    if gols_na_casa_asversario2 > gols_na_casa_asversario1:
        return "Time 2"
    return "Penaltis"


def main():
    n = int(input())
    for _ in range(n):
        time1jogo1, time2jogo1 = [int(x) for x in input().split(" x ")]
        time2jogo2, time1jogo2 = [int(x) for x in input().split(" x ")]
        result = solve(time1jogo1, time2jogo1, time2jogo2, time1jogo2)
        print(result)


if __name__ == '__main__':
    main()
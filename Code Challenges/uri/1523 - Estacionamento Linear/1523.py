ENTRADA = 42
SAIDA = 100


class Info:
    def __init__(self, tipo, horario, id):
        self.tipo = tipo
        self.horario = horario
        self.id = id


while True:
    n, k = [int(x) for x in input().split()]
    if n == k == 0: break
    infos = []
    for i in range(n):
        entrada, saida = [int(x) for x in input().split()]
        infos.append(Info(ENTRADA, entrada, i))
        infos.append(Info(SAIDA, saida, i))

    infos.sort(key=lambda carro: (carro.horario, carro.id))

    estacionamento = []
    possivel = True
    for info in infos:
        if info.tipo == ENTRADA:
            estacionamento.append(info)
            if len(estacionamento) > k:
                possivel = False
                break
        else:
            carro = estacionamento.pop()
            if carro.id != info.id:
                possivel = False
                break

    print("Sim") if possivel else print("Nao")



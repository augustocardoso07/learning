from queue import PriorityQueue

pri = {
    "VERMELHO": 0,
    "LARANJA": 1,
    "AMARELO": 2,
    "VERDE": 3,
    "AZUL": 4
}

def main():
    fila = PriorityQueue()
    count = 1
    while True:
        try:
            inpu = input()
        except EOFError:
            break
        if inpu == "beep":
            prioridade, chegada, id = fila.get()
            print(id)
        else:
            id, prioridade = inpu.split()
            prioridade = pri[prioridade]
            fila.put((prioridade, count, id))
            count += 1


if __name__ == '__main__':
    main()
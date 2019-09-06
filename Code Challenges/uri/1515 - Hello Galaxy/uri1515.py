def main():
    while True:
        n = int(input())
        if n == 0: break
        mensagens = []
        for _ in range(n):
            planeta, ano, tempo = input().split()
            mensagens.append((int(ano) - int(tempo), planeta))
        tempo, planeta = min(mensagens)
        print(planeta)


if __name__ == '__main__':
    main()
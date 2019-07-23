while True:
    n = int(input())
    if n == 0: break
    linha = input()
    mary = linha.count("0")
    john = linha.count("1")
    print("Mary won {} times and John won {} times".format(mary, john))
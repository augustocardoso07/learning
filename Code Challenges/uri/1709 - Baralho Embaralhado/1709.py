p = int(input())

cout = 0
deslocamento = list(range(1, int(p/2) + 1)) + list(range(-int(p/2), 0))
#print(deslocamento)
lista = [0] * p
lista[0] = "A"

i = 0

while True:
    #print(lista)
    next = i + deslocamento[i]
    lista[i], lista[next] = lista[next], lista[i]
    i = next
    cout += 1
    if lista[0] == "A": break

print(cout)
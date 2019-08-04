n = int(input())
preco = 0
total_kg = 0
for i in range(1, n + 1):
    preco += float(input())
    dia_kg = len(input().split())
    print("day {}: {} kg".format(i, dia_kg))
    total_kg += dia_kg
print("{:.2f} kg by day".format(total_kg / n))
print("R$ {:.2f} by day".format(preco /n))


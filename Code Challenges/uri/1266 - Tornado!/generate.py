def linha(n):
    result = ""
    binario = str(bin(i))[2:]
    if len(binario) == 1: binario = "000000" + binario
    if len(binario) == 2: binario = "00000" + binario
    if len(binario) == 3: binario = "0000" + binario
    if len(binario) == 4: binario = "000" + binario
    if len(binario) == 5: binario = "00" + binario
    if len(binario) == 6: binario = "0" + binario
    for v in binario:
        result += v + " "
    return result.strip()


for i in range(2 ** 7):
    print(7)
    print(linha(i))
print(0)
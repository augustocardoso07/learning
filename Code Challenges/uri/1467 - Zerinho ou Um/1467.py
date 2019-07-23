while True:
    try:
        a, b, c = [int(x) for x in input().split()]
    except:
        break
    if a == b == c: print("*")
    elif a == b: print("C")
    elif a == c: print("B")
    elif b == c: print("A")
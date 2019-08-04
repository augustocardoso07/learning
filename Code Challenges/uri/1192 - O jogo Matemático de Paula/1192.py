for _ in range(int(input())):
    a, op, b = input()
    a, b = int(a), int(b)
    if a == b:
        print(a * b)
    elif op.islower():
        print(a + b)
    else:
        print(b - a)
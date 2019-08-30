from math import trunc, ceil, floor

def main():
    while True:
        line = input()
        if line == "0": break
        q, d, p = [int(x) for x in line.split()]
        r = (q * d) / (1.0 - q/p)
        r = r + 0.001 if r > 0 else r - 0.001
        print("{} paginas".format(trunc(r)) if int(r) != 1 else "1 pagina")


if __name__ == '__main__':
    main()

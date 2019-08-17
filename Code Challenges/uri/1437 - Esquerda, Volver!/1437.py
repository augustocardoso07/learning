faces = ["N", "L", "S", "O"]


def main():
    while True:
        n = int(input())
        if n == 0: break
        comando = input()
        d = comando.count("D") % 4
        e = comando.count("E") % 4
        result = d - e
        print(faces[result])


if __name__ == '__main__':
    main()
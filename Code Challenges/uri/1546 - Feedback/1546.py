d = {
    1: "Rolien",
    2: "Naej",
    3: "Elehcim",
    4: "Odranoel"

}


def main():
    n = int(input())
    for _ in range(n):
        k = int(input())
        for _ in range(k):
            equipe = int(input())
            print(d[equipe])


if __name__ == '__main__':
    main()
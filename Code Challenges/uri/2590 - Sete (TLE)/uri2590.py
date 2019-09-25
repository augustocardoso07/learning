d = {0:1, 1:7, 2:9, 3:3}


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(d[n % 4])


if __name__ == '__main__':
    main()
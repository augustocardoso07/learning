def main():
    while True:
        a, b = [int(x) for x in input().split()]
        if 0 == a == b: break
        alice = {int(x) for x in input().split()}
        beatriz = {int(x) for x in input().split()}
        troca_alice = len(alice.difference(beatriz))
        troca_beatriz = len(beatriz.difference(alice))
        print(min(troca_alice, troca_beatriz))


if __name__ == '__main__':
    main()
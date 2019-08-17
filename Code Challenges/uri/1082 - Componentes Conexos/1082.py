from string import ascii_letters


def dfs(v, d):
    vizinhos = [v]
    result = set()

    while len(vizinhos) != 0:
        v = vizinhos.pop()
        result.add(v)

        for u in d[v]:
            if u not in result:
                vizinhos.append(u)
    return sorted(list(result))

def main():
    n = int(input())

    for i in range(1, n + 1):
        a, v = [int(x) for x in input().split()]
        d = dict()

        for j in range(a):
            letter = ascii_letters[j]
            d[letter] = []

        for _ in range(v):
            a, b = input().split()
            #print(a, b)
            d[a] = d.get(a, []) + [b]
            d[b] = d.get(b, []) + [a]

        print("Case #{}:".format(i))
        visitados = set()

        count = 0
        #print(d)
        for key, value in sorted(list(d.items())):
            #print(key, value)
            if not key in visitados:
                componentes = dfs(key, d)
                visitados = visitados.union(componentes)
                print(*componentes, sep=",", end=",\n")
                count += 1
        print("{} connected components".format(count))
        print()


if __name__ == '__main__':
    main()


def test_all(capsys):
    import sys, glob

    ins = sorted(glob.glob("in*"))
    outs = sorted(glob.glob("out*"))

    assert len(ins) == len(outs)

    for i in range(len(ins)):
        pathin = ins[i]
        pathout = outs[i]

        sys.stdin = open(pathin)
        main()
        out, err = capsys.readouterr()
        expected = open(pathout).read()
        assert out == expected
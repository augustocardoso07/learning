def main():
    n = int(input())
    print(n + 1)

if __name__ == '__main__':
    main()


def test_all(capsys):
    import sys
    from glob import glob

    ins = sorted(glob("in*"))
    outs = sorted(glob("out*"))

    with capsys.disabled():
        print()
        print("Arquivos testados: ", ins, outs)

    assert len(ins) == len(outs)

    for i in range(len(ins)):
        pathin = ins[i]
        pathout = outs[i]
        sys.stdin = open(pathin)
        main()
        out, err = capsys.readouterr()
        expected = open(pathout).read()
        assert out == expected
        with capsys.disabled():
            print("Teste {} ok!".format(i + 1))

    sys.stdin = sys.__stdin__
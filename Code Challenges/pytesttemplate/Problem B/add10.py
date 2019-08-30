def main():
    n = int(input())
    print(n + 10)


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
        assert expected == out
        with capsys.disabled():
            print("Teste {} ok!".format(i + 1))

    sys.stdin = sys.__stdin__


def test_all2(capsys):
    import sys
    from glob import glob

    ins = sorted(glob("in*"))
    outs = sorted(glob("out*"))

    with capsys.disabled():
        print()
        print("Arquivos testados: ", ins, outs)

    assert len(ins) == len(outs)

    all_test_pass = True
    for i in range(len(ins)):
        pathin = ins[i]
        pathout = outs[i]
        sys.stdin = open(pathin)
        main()
        out, err = capsys.readouterr()
        expected = open(pathout).read()
        if expected == out:
            with capsys.disabled():
                print("Teste {} ok!".format(i + 1))
        else:
            all_test_pass = False
            with capsys.disabled():
                print(":( Teste {} FALHOU <-----".format(i + 1))
                print("Resposta    Esperada: ", expected.__repr__())
                print("Resposta do programa: ", out.__repr__())

    assert all_test_pass

    sys.stdin = sys.__stdin__
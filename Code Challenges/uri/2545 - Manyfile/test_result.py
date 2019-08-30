import sys, glob, pytest
import uri2545

input_partner = "in*"
myoutput_file = "myout{}"
myoutput_partner = "myout*"
output_partner = "out*"

ins = sorted(glob.glob(input_partner))

for i in range(len(ins)):
    sys.stdin = open(ins[i])
    sys.stdout = open(myoutput_file.format(i + 1), "w")
    uri2545.main()

sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__

files_my_outs = sorted(glob.glob(myoutput_partner))
files_outs = sorted(glob.glob(output_partner))

outs = [open(file).read() for file in files_outs]
myouts = [open(file).read() for file in files_my_outs]
argvalues = zip(myouts, outs)


@pytest.mark.parametrize("result,expected", argvalues, ids=ins)
def test_all(result, expected):
    print()
    print(files_my_outs, files_outs)
    assert result == expected


def test_one():
    fileid = 1
    assert myouts[fileid - 1] == outs[fileid - 1]


if __name__ == '__main__':
    pass



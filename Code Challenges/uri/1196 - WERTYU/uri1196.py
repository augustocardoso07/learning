d = {
    " ": " ",
    "`": " ",
    "1": "`",
    "2": "1",
    "3": "2",
    "4": "3",
    "5": "4",
    "6": "5",
    "7": "6",
    "8": "7",
    "9": "8",
    "0": "9",
    "-": "0",
    "=": "-",
    "Q": "Q",
    "W": "Q",
    "E": "W",
    "R": "E",
    "T": "R",
    "Y": "T",
    "U": "Y",
    "I": "U",
    "O": "I",
    "P": "O",
    "[": "P",
    "]": "[",
    "\\": "]",
    "A": "A",
    "S": "A",
    "D": "S",
    "F": "D",
    "G": "F",
    "H": "G",
    "J": "H",
    "K": "J",
    "L": "K",
    ";": "L",
    "'": ";",
    "Z": "Z",
    "X": "Z",
    "C": "X",
    "V": "C",
    "B": "V",
    "N": "B",
    "M": "N",
    ",": "M",
    ".": ",",
    "/": ".",
}

def main():
    while 1:
        try:
            frase = input()
        except EOFError:
            break
        result = ""
        for letra in frase:
            result += d[letra]
        print(result)


if __name__ == '__main__':
    main()
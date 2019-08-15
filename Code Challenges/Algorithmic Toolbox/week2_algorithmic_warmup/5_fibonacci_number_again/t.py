def main():
    result =[0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764]
    n = range(len(result))
    rangeparams = range(-10, 11)
    for a in rangeparams:
        for b in rangeparams:
            for c in rangeparams:
                for d in rangeparams:
                    for e in rangeparams:
                        for x in n:
                            try:
                                if result[x] in [0,1,2,4,7]: continue
                                if result[x] == a ** (x - b) + c ** (x - d) + e:
                                    print(a, b, c, d, e, result[x])
                            except ZeroDivisionError:
                                pass
    print('end')

if __name__ == '__main__':
    main()
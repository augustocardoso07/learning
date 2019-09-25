import uri2590

print("d = {")
for i in range(10 ** 9 + 1):
    print("{}:{},".format(i, uri2590.solve(i)))
print("}")
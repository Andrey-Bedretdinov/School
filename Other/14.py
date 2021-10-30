number = str(hex(4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49))
a = [0] * 10
for i in number:
    if '0' <= i <= '9':
        a[int(i)] += 1
print(a)

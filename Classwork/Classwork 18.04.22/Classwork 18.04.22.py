def f(a):
    a = bin(a)[2:]
    if a[-1] == '0':
        dop = bin(a.count('1'))[2:]
        a += dop
    else:
        a = '1' + a + '00'
    return int(a, 2)

maxim = 0
for i in range(10000):
    g = f(i)
    if g < 1000:
        maxim = min(maxim, g)

print(maxim)

# a = (3 + 2 * 4**x) * 4**x + 3 + 4**y
def f(n):
    summa = 0
    while n != 0:
        summa += n % 4
        n //= 4
    return summa


maxim = 0
for x in range(200):
    for y in range(100):
        a = (3 + 2 * 4**x) * 4**x + 3 + 4**y
        h = f(a)
        if maxim < h:
            maxim = h
print(maxim)

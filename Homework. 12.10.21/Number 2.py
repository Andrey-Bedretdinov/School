def f(n):
    summa = 2 * n + 1
    if n > 1:
        summa += 3 * n - 8 + f(n - 1) + f(n - 4)
    return summa


a = 0
res = f(a)
while res <= 5000000:
    a += 1
    res = f(a)
print(a, res)


def f(n):
    summa = n * n
    if n > 1:
        summa += 2 * n + 1 + f(n - 2) + f(n // 3)
    return summa


a = 1
res = f(a)
while res <= 3200000:
    a += 1
    res = f(a)
print(a, res)

def f(n):
    summa = n - 5
    if n > 1:
        summa += n + 8 + f(n - 2) + f(n - 3)
    return summa


a = 1
while f(a) <= 3200000:
    a += 1
print(a, f(a))

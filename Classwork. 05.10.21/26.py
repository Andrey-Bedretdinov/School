def f(n):
    summa = n + 1
    if n > 1:
        summa += n + 5 + f(n - 1) + f(n - 2)
    return summa


a = 1
while f(a) <= 1000000:
    a += 1
print(a, f(a))

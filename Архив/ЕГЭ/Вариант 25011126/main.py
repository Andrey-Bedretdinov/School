n, m = 1000, 5  # Кол-во и в сумку
a = [40] * 1000  # Пробирки
for i in range(n):  # Cумки вместо пробирок
    if a[i] % m == 0:
        a[i] //= m
    else:
        a[i] = a[i] // m + 1
cena = 0
for i in range(n):
    cena += a[i] * i
mini = cena
bs = 0
fs = sum(a[1:])
for i in range(1, n):
    bs += a[i - 1]
    cena = cena - fs + bs
    fs -= a[i]


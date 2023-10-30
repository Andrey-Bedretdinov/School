with open('27-B.txt') as file:
    n = int(file.readline())
    data = [int(file.readline()) for i in range(n)]

cena = 0
for i in range(n):
    r = min(i, n - i)
    cena += r * data[i]

center = n // 2
bs = sum(data[center:])
fs = sum(data[1:center])
mini = cena
cont = None
for i in range(1, n):
    bs = bs + data[i - 1] - data[center]
    fs += data[center]
    cena = cena + bs - fs
    fs = fs - data[i]
    center = (center + 1) % n
    if cena < mini:
        mini = cena
        cont = i + 1

print(cont)

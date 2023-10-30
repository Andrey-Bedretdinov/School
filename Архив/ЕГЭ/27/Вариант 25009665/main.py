with open('27-B.txt') as file:
    n = int(file.readline())
    data = [int(file.readline()) for _ in range(n)]

cena = 0
for i in range(n):
    r = min(i, n - i)
    cena += data[i] * r

min_sum = cena
min_cont = 0
center = n // 2
bs = sum(data[center:])
fs = sum(data[1:center])
for i in range(1, n):
    bs = bs + data[i - 1] - data[center]
    fs += data[center]
    cena = cena + bs - fs
    fs -= data[i]
    center = (center + 1) % n
    if cena < min_sum:
        min_sum = cena
        min_cont = i + 1
print(min_cont, min_sum)



with open('27_B.txt') as file:
    n = int(file.readline())
    a = [[int(x) for x in file.readline().split(' ')] for _ in range(n)]

n = 10_000_000
data = [0] * n
for i in a:
    if i[1] % 36 == 0:  # Поменять значения!!!!!
        data[i[0]] = i[1] // 36
    else:
        data[i[0]] = i[1] // 36 + 1
print(data[:15])
cena = 0
for i in range(n):
    cena += data[i] * i

min_sum = cena
bs = 0
fs = sum(data[1:])
for i in range(1, n):
    bs += data[i - 1]
    cena = cena + bs - fs
    fs -= data[i]
    min_sum = min(min_sum, cena)
print(min_sum)


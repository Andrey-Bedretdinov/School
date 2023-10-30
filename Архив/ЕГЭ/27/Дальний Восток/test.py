with open('27_B.txt') as file:
    n = int(file.readline())
    data = [[int(x) for x in file.readline().split(' ')] for _ in range(n)]

cont = [0] * 10_000_000
for i in data:
    if i[1] % 36 == 0:
        cont[i[0]] = i[1] // 36
    else:
        cont[i[0]] = i[1] // 36 + 1

n = 10_000_000
cena = 0
for i in range(1, n):
    cena += cont[i] * i

min_sum = cena
bs = 0
fs = sum(cont[1:])
for i in range(1, n):
    bs += cont[i - 1]
    cena = cena + bs - fs
    fs -= cont[i]
    min_sum = min(min_sum, cena)
print(min_sum)

# Number 24
with open('24 (1).txt') as file:
    data = file.readline()

i = 0
count = 0
maxi = 0
while i <= len(data) - 2:
    a, b = data[i], data[i + 1]
    if a in ['B', 'C', 'D'] and b in ['A', 'O']:
        count += 1
        maxi = max(maxi, count)
        i += 2
    else:
        count = 0
        i += 1
print(maxi)




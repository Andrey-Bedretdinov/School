with open('27_A.txt') as file:
    n = int(file.readline())
    data = [[int(x) for x in file.readline().split(' ')] for _ in range(n)]

cd = {}  # словарь вместо списка
for i in data:
    cd[i[0]] = i[1]
km = sorted(cd)

max_km = max(km)
for i in range(max_km + 1):
    if not cd.get(i):
        cd[i] = 0

cd_sorted = {}
for i in range(max_km + 1):
    if cd[i] % 96 == 0:
        cd_sorted[i] = cd[i] // 36
    else:
        cd_sorted[i] = cd[i] // 36 + 1
data = list(cd_sorted.values())

cena = 0
for i in range(max_km + 1):
    cena += data[i] * i

min_sum = cena
cont = 0
bs = 0
fs = sum(data[1:])
n = len(data)
for i in range(1, n):
    bs += data[i - 1]
    cena = cena + bs - fs
    fs -= data[i]
    if cena < min_sum:
        min_sum = cena
        cont = i
print(cont, min_sum)
# 547 62885
# 4997603 5036401361477


# Number 26
with open('26.txt') as file:
    n = int(file.readline())
    data = [int(file.readline()) for x in range(n)]

data.sort(reverse=True)
count = 1
flag = data[0]

for i in range(1, len(data)):
    if flag - data[i] >= 3:
        count += 1
        flag = data[i]
print(count, flag)  # 2767 51


# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not (not (w <= z) or (x <= y) or not x):
                    print(x, y, z, w)


# Number 5
def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    return int(n, 2)


for i in range(100000):
    if f(i) >= 16:
        print(i)
        break


# Number 6
def f(s):
    s = (s - 21) // 10
    n = 1
    while s >= 0:
        n *= 2
        s -= n
    return n


for i in range(100000):
    if f(i) == 8:
        print(i)
        break


# Number 8
def cc(x, i):
    s = ''
    while x != 0:
        s = str(x % i) + s
        x //= i
    return s


count = 0
for i in range(100000000):
    s = cc(i, 8)
    if len(s) < 5:
        continue
    if len(s) > 5:
        break
    if s.count('6') == 1 and all(x not in s for x in ['16', '36', '56', '76', '96',
                                                      '61', '63', '65', '67', '69']):
        count += 1
print(count)


# Number 12
s = '9' * 96
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1)
    else:
        s = s.replace('9999', '2', 1)

print(s)


# Number 14
def cc(x, i):
    s = ''
    while x != 0:
        s = str(x % i) + s
        x //= i
    return s


a = 4 * 625**1920 + 4 * 125**1930 - 4 * 25**1940 - 3*5**1950 - 1960
a = cc(a, 5)
print(a.count('0'))


# Number 15
for a in range(1, 100000):
    for x in range(1, 10000):
        if not (((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)):
            break
    else:
        print(a)
        break


# Number 16
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 1) + n - 1
    if n > 2 and n % 2 != 0:
        return f(n - 2) + 2 * n - 2


print(f(34))


# Number 17
with open('17 (1).txt') as file:
    data = [int(line) for line in file]

mini = min(data)
count = 1
maxi = 0
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a % 117 == mini or b % 117 == mini:
        count += 1
        maxi = max(maxi, a + b)

print(count, maxi)


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 259:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'


for s in range(1, 245):
    print(s, f((17, s)))


# Number 22
def f(x):
    q, p, k1, k2 = 6, 10, 0, 0
    while x <= 100:
        k1 += 1
        x += p
    while x >= q:
        k2 += 1
        x -= q
    l = x + k1
    m = x + k2
    return l, m


for i in range(10000, 0, -1):
    if f(i) == (8, 21):
        print(i)
        break


# Number 23
def f(start, stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    return f(start - 1, stop) + f(start // 2, stop)


print(f(30, 12) * f(12, 1))


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


# Number 25
for i in range(10**20):
    a = int(f'1234{i}7')
    if a > 10**8:
        break
    if a % 141 == 0:
        print(a, a // 141)


















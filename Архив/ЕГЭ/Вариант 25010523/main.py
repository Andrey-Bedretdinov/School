# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not (not (y <= w) or x == z or x):
                    print(x, y, z, w)  # zywx


# Number 5
def f(n):
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '10' + n
    else:
        n = '1' + n + '01'
    return int(n, 2)


for i in range(100000):
    if f(i) >= 19:
        print(i)
        break


# Number 6
def f(s):
    s = (s - 21) // 10
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    return n


for i in range(10000, 1, -1):
    if f(i) == 16:
        print(i)
        break


# Number 12
s = '8' * 89
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '8', 1)
    else:
        s = s.replace('8888', '11', 1)
print(s)  # 118


# Number 14
def cc(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s

a = 5 * 216**3031 + 4 * 36**3042 - 3 * 6**3053 - 3064
a = cc(a, 6)

summ = 0
for i in a:
    summ += int(i)
print(summ)  # 30417


# Number 15
for a in range(1, 10000000):
    for x in range(1, 10000):
        if not (x % 2 != 0 or x % 5 != 0 or (x + a >= 90)):
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
    if n > 2 and n % 2 == 1:
        return f(n - 2) + 2 * n - 2


print(f(31))


# Number 17
with open('17 (1).txt') as file:
    data = [int(file.readline()) for _ in range(10000)]

minim = 10000000000
for i in data:
    if i % 6 == 0:
        minim = min(minim, i)

count = 0
ms = 0
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a % minim == 0 and b % minim == 0:
        count += 1
        ms = max(ms, a + b)
print(count, ms)  # 17 172728


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 247:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'
    return ''


for s in range(1, 234):
    print(s, f((17, s)))
    # 58
    # 106 114
    # 105


# Number 22
def f(x):
    q = 7
    p = 10
    k1 = 0
    k2 = 0
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
    if f(i) == (11, 20):
        print(i)  # 54
        break


# Number 23
def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    return f(start + 2, stop) + f(start * 2, stop)


print(f(1, 24) * f(24, 50))  # 64


# Number 24
with open('24 (4).txt') as file:
    data = file.read()

i = 0
count = 0
maxim = 0
while i <= len(data) - 2:
    ab = data[i] + data[i + 1]
    if ab in ['BA', 'DA']:
        count += 1
        maxim = max(maxim, count)
        i += 2
    else:
        count = 0
        i += 1
print(maxim)  # 151


# Number 25
for x in range(10):
    for y in range(10):
        a = int('1234' + str(x) + '57' + str(y) + '8')
        if a <= 10**9 and a % 17 == 0:
            print(a, a // 17)




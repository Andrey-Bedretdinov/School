# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not (not (x <= w) or y == z or y):
                    print(x, y, z, w)  # zxwy


# Number 5
def f(n):
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '10' + n
    else:
        n = '1' + n + '01'
    return int(n, 2)


for i in range(100000):
    if f(i) > 441:
        print(i)  # 47
        break


# Number 6
def f(s):
    s = (s - 21) // 10
    n = 1
    while s > 0:
        n *= 2
        s -= n
    return n


for i in range(100000):
    if f(i) == 32:
        print(i)  # 331
        break


# Number 12
s = '8' * 84
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '8', 1)
    else:
        s = s.replace('8888', '11', 1)

print(s)


# Number 14
def cc(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s


a = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
a = cc(a, 8)
print(a.count('7'))


# Number 15
for a in range(1, 100000):
    for x in range(1, 10000):
        if not (((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 90)):
            break
    else:
        print(a)  # 75
        break


# Number 16
def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return f(n - 2) + f(n - 1) - n
    if n > 2 and n % 2 == 1:
        return f(n - 1) - f(n - 2) + 2 * n


print(f(32))  # 3194


# Number 17
with open('17 (1).txt') as file:
    data = []
    for line in file:
        data.append(int(line))

mini = 10**20
for i in data:
    if i % 21 == 0:
        mini = min(mini, i)

count = 0
ms = 0
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a % mini == 0 or b % mini == 0:
        count += 1
        ms = max(ms, a + b)
print(count, ms)  # 126 171120


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 231:
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


for s in range(1, 216):
    print(s, f((17, s)))
    # 54
    # 98 106
    # 97


# Number 22
def f(x):
    q, p, k1, k2 = 8, 10, 0, 0
    while x <= 100:
        k1 += 1
        x += p
    while x >= q:
        k2 += 1
        x -= q
    l = x + k1
    m = x + k2
    return l, m


for i in range(1000, 1, -1):
    if f(i) == (12, 19):
        print(i)  # 53
        break


















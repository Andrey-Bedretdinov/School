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


# Number 23
def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    return f(start + 2, stop) + f(start * 2, stop)


print(f(1, 18) * f(18, 52))  # 96


# Number 24
with open('24 (1).txt') as file:
    data = file.readline()

i = 0
count = 0
maxi = 0
while i < len(data) - 1:
    ab = data[i] + data[i + 1]
    if ab in ['AB', 'CB']:
        count += 1
        maxi = max(maxi, count)
        i += 2
    else:
        count = 0
        i += 1
print(maxi)


# Number 25
for x in range(10):
    for y in range(10):
        a = int(f'12345{x}7{y}8')
        if a % 23 == 0 and a <= 10**9:
            print(a, a // 23)

# 123450798 5367426
# 123451718 5367466
# 123453788 5367556
# 123454708 5367596
# 123456778 5367686
# 123459768 5367816


# Number 26
with open('26.txt') as file:
    n = int(file.readline())
    data = []
    for _ in range(n):
        line = [int(x) for x in file.readline().strip('\n').split(' ')]
        data.append(line)

xy = {}
for i in data:
    if not xy.get(i[0]):
        xy[i[0]] = []
    xy[i[0]].append(i[1])
    xy[i[0]].sort()


maxi_x = 0
mini_y = 10**20
for x in xy:
    if len(xy[x]) < 2:
        continue

    for i in range(len(xy[x]) - 1):
        a, b = xy[x][i], xy[x][i + 1]
        if b - a - 1 == 3:  # Поменять на 13!!!
            maxi_x = x
            mini_y = a + 1
            break

print(maxi_x, mini_y)  # 56588 67073






















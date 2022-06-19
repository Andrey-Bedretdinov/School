# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not (((not x) or (y and (not z))) or w):
                    print(x, y, z, w)  # ywxz


# Number 5
def f(n):
    n = bin(n)[2:]
    if n[-1] == '1':
        n = '1' + n + '0'
    else:
        n = '11' + n + '11'
    return int(n, 2)


maxim = 0
for i in range(100000):
    a = f(i)
    if a < 126:
        maxim = max(maxim, a)
print(maxim)


# Number 6
def f(d):
    n = 3
    s = 57
    while s <= 1200:
        s = s + d
        n = n + 4
    return n


for i in range(1, 10000):
    if f(i) == 63:
        print(i)  # 77
        break


# Number 8
def cc(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s


count = 0
for a in range(100000000000000):
    k = cc(a, 9)
    if len(k) < 7:
        continue
    if len(k) > 7:
        break
    if (k[-1] not in ['3', '4', '7']) and all(tr not in k for tr in ['000', '111', '222', '333', '444', '555', '666',
                                                                     '777', '888', '999']):
        count += 1
print(count)  # 2676053


# Number 12
s = '1' * 81
while '1111' in s or '88888' in s:
    if '1111' in s:
        s = s.replace('1111', '888', 1)
    else:
        s = s.replace('88888', '888')
print(s)  # 88881


# Number 14
def cc(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s


a = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
a = cc(a, 5)
print(a.count('4'))  # 1484


# Number 16
def f(n):
    if n == 1:
        return 1
    if n > 1 and n % 2 == 1:
        return 3 * n + f(n - 2)
    if n > 1 and n % 2 == 0:
        return 4 * f(n / 2)


print(f(42))  # 1444


# Number 17
with open('17-4.txt') as file:
    data = []
    for line in file:
        data.append(int(line))

maxim = 0
for i in data:
    if i % 111 == 0:
        maxim = max(maxim, i)

count = 0
minim = 100000000000
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if (a > maxim or b > maxim) and (a % 10 == 7 or b % 10 == 7):
        count += 1
        minim = min(minim, a + b)
print(count, minim)  # 147 10849


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 211:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'


for s in range(1, 200):
    if f((17, s)) == 'В2':
        # print(s)
        pass

for s in range(1, 200):
    if f((17, s)) == 'П2':
        print(s)


# Number 22
def f(x):
    l, m = 0, 0
    while x > 0:
        m = m + 1
        if x % 2 != 0:
            l = l + 1
        x = x // 2
    return l, m


for i in range(1000000):
    if f(i) == (5, 8):
        print(i)  # 143
        break


# Number 23
def f(start, stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    return f(start - 2, stop) + f(start - 5, stop)


print(f(23, 2))


# Number 24
with open('24 (3).txt') as file:
    data = file.read()

i = 0
count = 0
maxim = 0
while i < len(data) - 2:
    abc = data[i] + data[i + 1] + data[i + 2]
    if abc in ['ZXY', 'ZYX']:
        count += 1
        maxim = max(maxim, count)
        i += 3
    else:
        i += 1
        count = 0
print(maxim)  # 28


# Number 25
for x in range(10):
    for y in range(10):
        a = int('12345' + str(x) + '6' + str(y) + '8')
        if a > 10**9:
            continue
        if a % 17 == 0:
            print(a, a // 17)


# Number 26
with open('26 (1).txt') as file:
    data = []
    for line in file:
        a, b = line.strip('\n').split(' ')
        data.append([int(a), int(b)])

xy = {}
for x in range(1, 101):
    xy[x] = [0] * 101

for i in data:
    xy[i[0]][i[1]] = 1

maxim = 0
maxim_x = 0
for x in xy:
    count = 0
    for i in range(len(xy[x]) - 1):
        a, b = xy[x][i], xy[x][i + 1]
        if a == 1 and b == 1:
            if count == 0:
                count = 2
            else:
                count += 1
                if count >= maxim:
                    maxim = count
                    maxim_x = x
        else:
            count = 0
print(maxim_x, maxim)  # 99 14
print(xy[99])







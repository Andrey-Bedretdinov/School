# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not ((not (x <= y)) or ((not w) <= (not z)) or w):
                    print(x, y, z, w)  # xywz

# Number 5
def f(n):
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '10' + n + '10'
    else:
        n = '1' + n + '10'
    return int(n, 2)


minim = 10000000000
for i in range(1000000):
    a = f(i)
    if a > 100 and a < minim:
        print(a)
        minim = min(minim, a)


# Number 6
def f(s):
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    return n


for s in range(100000, 0, -1):
    if f(s) == 1024:
        print(s)  # 14338
        break


# Number 12
def f(b):
    x, y = 0, 0
    x, y = x + 5, y - 1
    for n in range(1, 100):
        for _ in range(n):
            x, y = x - 2, y + b
            x, y = x + 7, y - 3
        x, y = x - 55, y + 131
        if x == 0 and y == 0:
            return True
        else:
            x, y = 0, 0
            x, y = x + 5, y - 1


for b in range(-1000, 10000000):
    if f(b):
        print(b)
        break


# Number 14
def step(x, i):
    s = ''
    while x > 0:
        ost = str(x % i)
        if ost == '10':
            s = 'A' + s
        elif ost == '11':
            s = 'B' + s
        elif ost == '12':
            s = 'C' + s
        elif ost == '13':
            s = 'D' + s
        else:
            s = ost + s
        x //= i
    return s


a = 2197**50 - 169**35 - 26
print(step(a, 13).count('C'))  # 147


# Number 15
def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False


for a in range(1, 10000000):
    for x in range(1000):
        if ((not deli(x, 15)) or (not deli(x, 28)) or deli(x, a)) and (a > 70):
            continue
        break
    else:
        print(a)  # 84
        break


# Number 16
def f(n):
    if n == 1:
        return 1
    if n > 1 and n % 2 == 0:
        return n * f(n - 1)
    if n > 1 and n % 2 == 1:
        return 1 + f(n - 2)


print(f(84))  # 3528


# Number 17
with open('17 (1).txt') as file:
    data = []
    for line in file:
        data.append(int(line))

maxim = 0
for i in data:
    if i > maxim and i % 11 == 0:
        maxim = max(maxim, i)

count = 0
minim_sum = 100000000000000
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a > maxim or b > maxim:
        count += 1
        minim_sum = min(minim_sum, a + b)
print(count, minim_sum)


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 3, b), (a * 2, b), (a, b + 3), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 300:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В1' or f(x) == 'В2' for x in moves(p)):
        return 'П2'
    if any(f(x) == 'П1' or f(x) == 'П2' for x in moves(p)):
        return 'В3'


for s in range(1, 305):
    if f((20, s)) == 'П1':
        # print(s)  # 139
        break

for s in range(1, 305):
    if f((20, s)) == 'В2':
        # print(s)  # 129 138
        pass

for s in range(1, 305):
    if f((20, s)) == 'В3':
        print(s)  # 63
        break


# Number 22
def f(x):
    a, b = 0, 0
    while x > 0:
        a += 1
        d = x % 10
        if d % 3 == 0:
            b += d
        x //= 10
    return a, b


for x in range(99999999999, 1000000000000000):
    if f(x) == (12, 99):
        print(x)


# Number 24
with open('24 (2).txt') as file:
    data = file.read()

count = 0
maxim = 0
i = 0
while i < len(data) - 2:
    a, b = data[i], data[i + 1]
    if a + b in ['BB', 'DD']:
        count += 1
        i += 2
        maxim = max(maxim, count)
        continue
    i += 1
    count = 0
print(maxim)  # 316


# Number 25
for i in range(100000000000000):
    a = int('12' + str(i) + '6789')
    if a > 10**8:
        break
    if a % 39 == 0:
        print(a, a//39)


# Number 26
with open('26.txt') as file:
    data = []
    for line in file:
        a, b = line.strip('\n').split(' ')
        data.append([int(a), int(b)])

xy = {}
for y in range(1, 10001):
    xy[y] = [0] * 10001

for i in data:
    xy[i[0]][i[1]] = 1

count = 0
maxim = 0
minim_y = 0
for y in xy:
    for x in range(0, 10000):
        a, b = xy[y][x], xy[y][x + 1]
        if a == 1 and b == 1:
            if count == 0:
                count += 2
            else:
                count += 1
            maxim = max(maxim, count)
    count = 0
    if maxim == 22:
        print(y)
        break
print(maxim)






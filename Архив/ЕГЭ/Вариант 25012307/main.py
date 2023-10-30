'''
# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if (x or y) and (y != z) and w:
                    print(x, y, z, w)  # zyxw

# Number 5
def f(n: int):
    if n in [0, 1]:
        n = '0'
    else:
        n = bin(n)[3:]
    if n.count('1') % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '0'
    return int(n, 2)

maxim = 0
for i in range(1, 10000000):
    a = f(i)
    if a < 450:
        maxim = max(maxim, f(i))
print(maxim)  # 444

# Number 6
def f(s):
    s = (s + 13) * 10
    n = 512
    while s < 0:
        n = n // 2
        s = s + n
    return n


for i in range(1000000000, 1000000000000000000000000):
    if f(i) == 8:
        print(i)
        break

# Number 14
a = 7 * 729*543 - 6 * 81**765 - 5 * 9**987 - 20
count = 0
while a != 0:
    if a % 9 == 8:
        count += 1
    a //= 9
print(count)  # 1625


# Number 16
def f(n):
    if n < 3:
        return n * 3
    if n > 2 and n % 2 == 0:
        return f(n - 2) * f(n - 1) - n
    if n > 2 and n % 2 == 1:
        return f(n - 1) - f(n - 2) + 2 * n

print(f(30) % 100)  # 36

# Number 17
with open('17 (1).txt') as file:
    numbers = []
    for line in file:
        numbers.append(int(line))

minim = 100000000
for i in numbers:
    if i % 103 == 0:
        minim = min(minim, i)


count = 0
maxim = 0
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if (a + b) % 2 == 0 and (a - b) % minim == 0:
        count += 1
        maxim = max(maxim, a + b)
print(count, maxim)

# Number 19 20 21
from functools import lru_cache
def moves(p):
    a, b = p
    return (a + 2, b), (a * 2, b), (a, b + 2), (a, b * 2)


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
    if all(f(x) in ['В1', 'В2'] for x in moves(p)):
        return 'П2'


for s in range(1, 216):
    if f((17, s)) == 'П1':
        print(s)

for s in range(1, 216):
    if f((17, s)) == 'В2':
        print(s)

for s in range(1, 216):
    if f((17, s)) == 'П2':
        print(s)


# Number 22
def f(x):
    k = 9*x - 57
    d = 9*x + 13
    while k * d > 0:
        if k > d:
            k = k % d
        else:
            d = d % k
    return k + d


for i in range(1000, 1, -1):
    if f(i) == 70:
        print(i)  # 963
        break


# Number 23
def f(start, stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    return f(start - 3, stop) + f(start // 2, stop)

print(f(108, 42) + f(42, 12))  # 11


# Number 24
with open('24 (1).txt') as file:
    s = file.read()

count = 0
maxim = 0
i = 0
try:
    while True:
        a, b = s[i], s[i + 1]
        if a + b == 'AB':
            count += 2
            maxim = max(maxim, count)
            i += 2
            continue
        c = s[i + 2]
        if a + b + c == 'CAC':
            count += 3
            maxim = max(maxim, count)
            i += 3
            continue
        i += 1
        count = 0
except:
    print(maxim)


# Number 25
def get_divs(a):
    divs = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            divs.add(i)
            divs.add(a // i)
    return list(divs)

for i in range(800001, 10000000000000):
    divs = get_divs(i)
    if len(divs) <= 10:
        continue
    umn = 1
    for div in divs:
        umn *= div
    if sum(divs) % 2 == 1 and umn % 2 == 1:
        print(i, len(divs))
        '''





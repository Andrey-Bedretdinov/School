# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not ((x <= y) or not (w <= z)):
                    print(x, y, z, w)  # zywx


# Number 5
def f(n):
    n = bin(n)[2:]
    if n.count('0') == n.count('1'):
        n += n[-1]
    elif n.count('0') < n.count('1'):
        n += '0'
    else:
        n += '1'

    if n.count('0') == n.count('1'):
        n += n[-1]
    elif n.count('0') < n.count('1'):
        n += '0'
    else:
        n += '1'

    return int(n, 2)


for i in range(99, 0, -1):
    a = f(i)
    if a % 4 == 0 and a % 8 != 0:
        print(i)
        break


# Number 6
def f(s):
    n = 1
    while s < 47:
        s += 4
        n *= 2
    return n


for i in range(100000, 0, -1):
    if f(i) == 64:
        print(i)
        break


# Number 8
count = 0
s = 'ВИШНЯ'
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('В') >= 1:
                            continue
                        if word[0] == 'Ш' or word[-1] in 'ИЯ':
                            continue
                        count += 1
print(count)


# Number 12
s = '1' * 95 + '7' * 31
while '1111' in s:
    s = s.replace('1111', '7', 1)
    s = s.replace('77', '1', 1)
print(s)


# Number 14
for n in range(4, 100000):
    if int('132', n) + int('13', 8) == int('124', n + 1):
        print(n)  # 6
        break


# Number 15
for a in range(10000000):
    for x in range(10000):
        if not (x % 2 != 0 or x % 5 != 0 or x + a >= 90):
            break
    else:
        print(a)
        break


# Number 16
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    if n > 1 and n % 2 == 1:
        return 2 * f(n - 2)


print(f(24))  # 2072


# Number 17
with open('17 (1).txt') as file:
    data = [int(line) for line in file]

maxim = 0
for i in data:
    if i % 11 == 0:
        maxim = max(maxim, i)

ms = 0
count = 0
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if (a % 11 == 0 or b % 11 == 0) and a + b <= maxim:
        count += 1
        ms = max(ms, a + b)
print(count, ms)  # 731 990


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 77:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'


for s in range(1, 75):
    if f((7, s)) == 'П2':
        print(s)


# Number 22
def f(x):
    a, b = 0, 0
    while x > 0:
        c = x % 10
        a = a + c
        if b < c:
            b = c
        x = x // 10
    return a, b


for i in range(100000):
    if f(i) == (10, 6):
        print(i)
        break


# Number 23
def f(start, stop):
    if start > stop or start == 15:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start * 2, stop)


print(f(2, 12) * f(12, 32))  # 30


# Number 24
with open('24 (4).txt') as file:
    data = file.read()

s = ''
maxim = 0
for i in data:
    s += i
    if '.' in s:
        if s.count('A') >= 3:
            maxim = max(maxim, len(s) - 1)
        s = ''
print(maxim)  # 284


# Number 25
def get_divs(n):
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return list(divs)


count = 0
for number in range(220001, 100000000000000):
    divs = get_divs(number)
    if not divs:
        m = 0
    else:
        m = min(divs) + max(divs)

    if m % 10 == 4:
        print(number, m)
        count += 1

    if count == 5:
        break





















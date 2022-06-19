# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not (not (z and not w) or (z <= w) == (x <= y)):
                    print(x, y, z, w)  # zxwy


# Number 5
def f(n):
    n = bin(n)[2:]
    if n[-1] == '0':
        n = '1' + n + '0'
    else:
        n = '11' + n + '10'
    return int(n, 2)


mini = 10**20
for i in range(0, 10000):
    r = f(i)
    r_ = r
    summ = 0
    while r != 0:
        summ += r % 10
        r //= 10
    if summ > 17:
        mini = min(mini, r_)
print(mini)  # 3


# Number 6
def f(s):
    n = 5
    while s < 110:
        s += n
        n += 1
    return n


for i in range(10000, 0, -1):
    if f(i) == 15:
        print(i)  # 28
        break


# Number 6
def f(s):
    n = 5
    while s < 110:
        s += n
        n += 1
    return n


for i in range(10000, 0, -1):
    if f(i) == 15:
        print(i)  # 28
        break


# Number 6
def f(s):
    n = 5
    while s < 110:
        s += n
        n += 1
    return n


for i in range(10000, 0, -1):
    if f(i) == 15:
        print(i)  # 28
        break


# Number 12
s = '2' * 400
while '8888' in s or '222' in s:
    if '222' in s:
        s = s.replace('222', '88', 1)
    else:
        s = s.replace('8888', '22', 1)

print(s)  # 882882


# Number 14
def cc(x, i):
    s = ''
    while x != 0:
        s = str(x % i) + s
        x //= i
    return s


a = 5**94 + 25**49 - 130
print(cc(a, 5).count('4'))  # 92


# Number 16
def f(n):
    if n < 5:
        return 1 + 2 * n
    if n >= 5 and n % 3 == 0:
        return 2 * (n + 1) * f(n - 2)
    if n >= 5 and n % 3 != 0:
        return 2 * n + 1 + f(n - 1) + 2 * f(n - 2)


print(f(15))  # 5158048


# Number 17
with open('17 (1).txt') as file:
    data = [int(line) for line in file]

maxi = 0
for i in data:
    if i % 111 == 0:
        maxi = max(maxi, i)

count = 0
mini = 10**20
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if any(x > maxi for x in [a, b]) and any(x % 10 == 7 for x in [a, b]):
        count += 1
        mini = min(mini, a + b)

print(count, mini)  # 147 10849


# Number 19 20 21
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(p):
    a, b = p
    if a * b >= 63:
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


for s in range(1, 32):
    print(s, f((2, s)))
    # 15
    # 7 14
    # 28


# Number 22
def f(x):
    a = 3 * x + 23
    b = 3 * x - 17
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


for i in range(6, 100000):

    if f(i) == 10:
        print(i)
        break


# Number 23
def f(start, stop):
    if start > stop or start == 30:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start * 3, stop) + f(start * 4, stop)


print(f(2, 15) * f(15, 100))  # 182


# Number 24
with open('24 (1).txt') as file:
    data = file.readline()

count = 0
maxi = 0
for i in range(len(data) - 1):
    ab = data[i] + data[i + 1]
    if ab not in ['PR', 'RP']:
        if count == 0:
            count += 2
        else:
            count += 1
            maxi = max(maxi, count)
    else:
        count = 0
print(maxi)  # 2940


# Number 26
with open('26.txt') as file:
    n = int(file.readline())
    data = []
    for line in file:
        data.append([int(x) for x in line.strip('\n').split(' ')])

xy = {}
for i in data:
    if not xy.get(i[0]):
        xy[i[0]] = []
    xy[i[0]].append(i[1])
    xy[i[0]].sort()

maxi = 0
max_x = 0
for x in xy:
    count = 0
    if len(xy[x]) > 1:
        for y in range(len(xy[x]) - 1):
            a, b = xy[x][y], xy[x][y + 1]
            if b - a == 1:
                if count == 0:
                    count += 2
                else:
                    count += 1
                    if count >= maxi:
                        maxi = count
                        max_x = x
            else:
                count = 0

print(max_x, maxi)  # 24 14









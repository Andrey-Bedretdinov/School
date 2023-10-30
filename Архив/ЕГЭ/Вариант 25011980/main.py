# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not w and ((y or z) <= (y and not x)) and [x, y, z, w] != [0, 0, 0, 0]:
                    print(x, y, z, w)  # wzyx


# Number 5
def f(n):
    n = bin(n)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    return int(n, 2)


mini = 10**20
for i in range(10000):
    if f(i) > 396:
        mini = min(mini, f(i))
print(mini)  # 402


# Number 6
def f(s):
    n = 34
    while n <= 170:
        s += 120
        n += 23
    return s


for i in range(1000000):
    if len(str(f(i))) == 4:
        print(i)  # 280
        break


# Number 8
def cc(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s


count = 0
for j in range(100000):
    w = cc(j, 7)
    if len(w) != 4 and w != '1000' and w != '1001':
        continue
    if all(not d in w for d in ['11', '22', '33', '44', '55', '66', '77', '88', '99']):
        count += 1
print(count)  # 1368


# Number 12
s = '4' * 23 + '5' * 12 + '53' * 17

while '43' in s or '53' in s:
    if '43' in s:
        s = s.replace('43', '33', 1)
    else:
        s = s.replace('53', '433', 1)

print(s.count('3'))  # 98


# Number 14
def cc(x, i):
    s = ''
    while x > 0:
        ost = x % i
        if ost > 9:
            s = '?' + s
        else:
            s = str(ost) + s
        x //= i
    return s


a = 6 * 512**180 + 7 * 64**181 + 3 * 8**184 + 5 * 8**125 - 65
print(cc(a, 64).count('0'))  # 205


# Number 15
for a in range(1000, 0, -1):
    flag = True
    for x in range(100):
        for y in range(100):
            if x < a and y < a and x * y > 1200:
                flag = False
                break
        else:
            continue
        break
    if flag:
        print(a)  # 35
        break


# Number 16
def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 == 1:
        return f(3 * n + 1) + 1


count = 0
for i in range(1, 100001):
    if f(i) == 16:
        count += 1
print(count)


# Number 17
with open('17 (1).txt') as file:
    data = [int(file.readline()) for _ in range(2000)]

sr = sum(data) / len(data)
count = 0
ms = 0
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a < sr and b < sr and (a % 10 == 9 or b % 10 == 9):
        count += 1
        ms = max(ms, a + b)

print(count, ms)  # 86 10184


# Number 19 20 21
from functools import lru_cache


def moves(p):
    return p + 1, p + 4, p * 2


@lru_cache(None)
def f(p):
    if p >= 40:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'


for s in range(1, 44):
    print(s, f(s))
    # 19
    # 15 18
    # 14


# Number 22
def f(x):
    a, b = 0, 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 6
        x //= 6
    return a, b


for i in range(0, 10000000):
    if f(i) == (1, 4):
        print(i)  # 39
        break


# Number 23
def f(start, stop):
    if start > stop or start == 11 or start == 18:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start + 2, stop) + f(start * 3, stop)


print(f(4, 8) * f(8, 23))

# Number 24
with open('24 (5).txt') as file:
    data = file.readline()

i = 1
count = 0
maxi = 0
while i <= len(data) - 1:
    a, b, c = data[i - 1], data[i], data[i + 1]
    if a in 'XZ' and c == 'Y':
        count += 1
        maxi = max(maxi, count)
        i += 3
    else:
        count = 0
        i += 1

print(maxi)  # 19


# Number 25
for y in range(10):
    a = int(f'123567{y}')
    if a % 169 == 0:
        print(a, a // 169)

flag = True
for x in range(10**20):
    for y in range(10):
        a = int(f'123{x}567{y}')
        if a > 10**9:
            flag = False
            break
        if a % 169 == 0:
            print(a, a // 169)

    if not flag:
        break


# Number 26
with open('26 (1).txt') as file:
    n, t = [int(x) for x in file.readline().strip('\n').split(' ')]
    data = []
    for _ in range(n):
        data.append([int(x) for x in file.readline().strip('\n').split(' ')])

summ = 0
for i in data:
    summ += i[0]
sr = int(summ / len(data)) + 1

virus = []
super_virus = []
for i in data:
    if i[0] >= sr:
        super_virus.append(i[1])
    else:
        virus.append(i[1])

virus.sort()
super_virus.sort()

count = 0
super_t = 0
t_now = 0
super = False

while t_now < t:
    if not super and super_virus and virus and t_now + super_virus[0] + virus[0] <= t:
        time = super_virus[0]
        super_virus.remove(time)

        count += 1
        super_t += time
        t_now += time
        super = True

    elif virus and t_now + virus[0] <= t:
        time = virus[0]
        virus.remove(time)

        count += 1
        t_now += time
        super = False

    else:
        break

print(count, super_t)  # 4717 5538526









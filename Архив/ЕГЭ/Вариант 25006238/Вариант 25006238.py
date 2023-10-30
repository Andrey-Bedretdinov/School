from functools import lru_cache

print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not ((x and z) or (((not w) or x) == ((not z) or y))) and w == 1:
                    print(x, y, z, w)

print('----------')


def f(d):
    n = 10
    s = 101
    while d < s + n:
        s -= 2 * d
        n += d
    return n


for i in range(1, 100000):
    if f(i) == 100:
        print(i)
        break

print('----------')


def f(a_):
    a_ = bin(a_)[2:]
    if a_.count('1') > a_.count('0'):
        a_ += '0'
    else:
        a_ = '11' + a_
    return int(a_, 2)


for i in range(1, 1000000):
    if f(f(i)) > 500:
        print(i)
        break

print('----------')

count = 0
letters = 'ГАФНИЙ'
for a1 in letters:
    for a2 in letters:
        for a3 in letters:
            for a4 in letters:
                word = a1 + a2 + a3 + a4
                if word[0] != 'Й' and (word.count('А') >= 1 or word.count('И') >= 1):
                    count += 1
print(count)

print('----------')

s = 'X' * 107
while 'XXX' in s or 'ZYX' in s or 'ZXX' in s:
    s = s.replace('XXX', 'ZZ', 1)
    s = s.replace('ZYX', 'X', 1)
    s = s.replace('ZXX', 'Y', 1)
print(s)

print('----------')

a = 5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3
count = 0
while a != 0:
    if a % 7 == 0:
        count += 1
    a //= 7
print(count)

print('----------')

count = 0
for a in range(1, 10000):
    for x in range(1, 10000):
        if not((a % 5 == 0) and ((2020 % a == 0) or ((x % 1728 != 0) or (2023 % a == 0)))):
            break
    else:
        count += 1
print(count)

print('----------')


def f(n):
    if n <= 70:
        return f(n + 2) + 2 * f(n * 3)
    if n > 70:
        return n - 50


print(f(40))

print('----------')

count = 0
maxim = 0
for i in range(4563, 7913):
    if i % 7 == 0 and i % 10 + i // 1000 > 10:
        count += 1
        maxim = i
print(maxim, count)

print('----------')


def moves(p):
    return p + 1, p * 2, p * 3


@lru_cache()
def f(p):
    if p > 72:
        return 'В1'
    if p >= 43:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'
    if any(f(x) == 'П2' or f(x) == 'П1' for x in moves(p)):
        return 'В3'


for i in range(1, 50):
    if f(i) == 'П1':
        print(i)
        break

count = 0
for i in range(1, 43):
    if f(i) == 'В2':
        count += 1
print(count)

ans = []
for i in range(1, 43):
    if f(i) == 'П2':
        ans.append(i)
print(min(ans), max(ans))

print('----------')


def f(x):
    q = 9
    l = 0
    while x >= q:
        l += 1
        x -= q
    m = x
    if m < l:
        m = l
        l = x
    return l, m


for i in range(10000, 0, -1):
    if f(i) == (4, 5):
        print(i)
        break

print('----------')


def f(start, stop):
    if start > stop or start == 12:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start + 3, stop)


print(f(7, 27) * f(27, 50))

print('----------')

file = open('24.txt')
data = file.read()
file.close()
count = 1
max_count = 0
max_s = 0
for i in range(1, len(data)):
    if data[i] < data[i - 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        if max_count == count:
            max_s = i
        count = 1
print(max_s - max_count + 1)

print('----------')

for i in range(106732567, 152673837):
    if i**0.5 % 1 != 0:
        continue
    divs = set()
    for div in range(2, int(i**0.5) + 1):
        if i % div == 0:
            divs.add(div)
            divs.add(i // div)
    if len(divs) == 3:
        print(i, max(divs))

print('----------')

numbers = []
for i in open('26.txt'):
    numbers.append(int(i))
numbers.sort()
for i in range(50):
    numbers.remove(numbers[0])
    numbers.remove(numbers[-1])
print(max(numbers), int(sum(numbers) / len(numbers)))

print('----------')

numbers = []
for i in open('27-A.txt'):
    numbers.append(int(i))
numbers.sort(reverse=True)
maxim = 0
for i in range(10):
    if numbers.count(i) % 2 != 0:
        numbers.remove(i)
        maxim = max(maxim, i)
ans = str(maxim)
numbers.remove(0)
numbers.remove(0)
while len(numbers):
    for i in range(10):
        for k in range(numbers.count(i) // 2):
            ans = str(i) + ans + str(i)
            numbers.remove(i)
            numbers.remove(i)
summa = 0
for i in ans:
    summa += int(i)
print(f'0{ans}0', summa)


numbers = []
for i in open('27-B.txt'):
    numbers.append(int(i))
numbers.sort(reverse=True)
maxim = 0
for i in range(10):
    if numbers.count(i) % 2 != 0:
        numbers.remove(i)
        maxim = max(maxim, i)
ans = str(maxim)
numbers.remove(5)
numbers.remove(5)
while len(numbers):
    for i in range(10):
        for k in range(numbers.count(i) // 2):
            ans = str(i) + ans + str(i)
            numbers.remove(i)
            numbers.remove(i)
ans = f'5{ans}5'
summa = 0
for i in ans:
    summa += int(i)
print(summa)

'''
    1) 30
    2) xzyw
    3) 44
    4) 38
    5) 32
    6) 30
    7) 16
    8) 888
    9) 942
    10) 110
    11) 18
    12) XX
    13) 4
    14) 10
    15) 6
    16) 3702
    17) 7896 225
    18) 1495 -2371
    19) 14
    20) 3
    21) 12 39
    22) 49
    23) 2100006
    24) 44701
    25) 112550881 1092727
        131079601 1225043
        141158161 1295029
    26) 957 501
    27) 61 254363
'''

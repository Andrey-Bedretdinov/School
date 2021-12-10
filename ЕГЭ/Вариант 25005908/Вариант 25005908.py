from functools import lru_cache

print('# Number 2')
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if (x and (y or (not z)) and w) == ((not x) or ((not y) and z)):
                    print(x, y, z, w)

print('---------')


def f(s):
    n = 1
    while s < 80:
        s += 7
        n *= 3
    return n


print('# Number 6')
for i in range(10000, 0, -1):
    if f(i) == 27:
        print(i)
        break

print('----------')


def f(a):
    ans = ''
    while a != 0:
        ans = str(a % 5) + ans
        a //= 5
    return ans


print('# Number 8')
count = 0
for i in range(3125, 15625):
    if f(i)[-1] != '3' and f(i)[-1] != '4' and f(i)[0] != '1':
        count += 1
print(count)

print('---------')

print('# Number 12')
s = '23' * 30 + '1' * 30
while '21' in s or '23' in s:
    if '21' in s:
        s = s.replace('21', '11', 1)
    else:
        s = s.replace('23', '21', 1)
print(s.count('1'))

print('---------')

print('# Number 14')
a = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
a6 = ''
while a != 0:
    a6 = str(a % 6) + a6
    a //= 6
print(a6.count('5') - a6.count('0'))

print('---------')

print('# Number 15')
count = 0
for a in range(1, 1001):
    for x in range(1, 10000):
        if not ((a % 9 == 0) and ((280 % x != 0) or ((a % x == 0) or (730 % x != 0)))):
            break
    else:
        count += 1
print(count)

print('---------')


def f(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 1) + n


print('# Number 16')
count = 0
for i in range(1, 100000 + 1):
    if f(i) == 16:
        count += 1
print(count)

print('---------')

print('# Number 17')
count = 0
minim = 1000000000000
for i in range(3072, 7320 + 1):
    if i % 10 == 5 and (i % 7 == 0 or i % 11 == 0 or i % 13 == 0):
        count += 1
        minim = min(minim, i)
print(count, minim)

print('---------')


def muves(p):
    return p * 2, p * 3


@lru_cache(None)
def f(p):
    if p >= 100:
        return 'WIN'
    if any(f(x) == 'WIN' for x in muves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in muves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in muves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in muves(p)):
        return 'П2'
    if any(f(x) == 'П2' or f(x) == 'П1' for x in muves(p)):
        return 'В3'


print('# Number 19, 20, 21')
for i in range(1, 102):
    if f(i) == 'В1' and i % 3 == 0:
        print(i, i // 3, end=' | ')
        break

for i in range(1, 102):
    if f(i) == 'В2':
        print(i, end=' ')

for i in range(1, 102):
    if f(i) == 'П2':
        print('|', i)
        break

print('----------')


def f(a):
    r = 17
    l = 0
    while a >= r:
        l += 1
        a -= r
    m = a
    if m < l:
        m = l
        l = a
    return l, m


print('# Number 22')
for i in range(10000, 0, -1):
    if f(i) == (11, 14):
        print(i)
        break

print('-----------')


def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    if start < stop:
        return f(start + 1, stop) + f(start * 2, stop)


print('# Number 23')
print(f(2, 7) * f(7, 16) * f(16, 39))

print('-----------')

print('# Number 24')
file = open('24 (25005908).txt')
data = file.read()
file.close()
count = 0
maxim = 0
for i in range(len(data)):
    if data[i] in 'WRQ':
        count = 0
    else:
        count += 1
    maxim = max(maxim, count)
print(maxim)

print('-----------')


def is_simple(a):
    for div in range(2, int(a ** 0.5) + 1):
        if a % div == 0:
            return False
    return True


print('# Number 25')
k = 5
for i in range(250001, 10000000000):
    divs = set()
    if k == 0:
        break
    for div in range(2, int(i**0.5) + 1):
        if i % div == 0:
            if is_simple(div):
                divs.add(div)
            if is_simple(i // div):
                divs.add(i // div)
    if sum(divs) != 0 and sum(divs) % 17 == 0:
        print(i, sum(divs))
        k -= 1

print('-----------')

print('# Number 26')
numbers = []
for i in open('26 (25005908).txt'):
    numbers.append(int(i))
d1 = []
d2 = []
for i in range(10000):
    count = numbers.count(i)
    while count / 2 >= 1:
        d1.append(i)
        d2.append(i)
        numbers.remove(i)
        numbers.remove(i)
        count -= 2

print(len(numbers), end=' ')

while len(numbers):
    if sum(d1) > sum(d2):
        d2.append(max(numbers))
        numbers.remove(max(numbers))
        d2.append(max(numbers))
        numbers.remove(max(numbers))
        d1.append(min(numbers))
        numbers.remove(min(numbers))
        d1.append(min(numbers))
        numbers.remove(min(numbers))
    else:
        try:
            d1.append(max(numbers))
            numbers.remove(max(numbers))
            d1.append(max(numbers))
            numbers.remove(max(numbers))
            d2.append(min(numbers))
            numbers.remove(min(numbers))
            d2.append(min(numbers))
            numbers.remove(min(numbers))
        except Exception as ex:
            print(ex)
print(abs(sum(d1) - sum(d2)))

print('-------------')

print('# Number 27')
data = []
for i in open('27-A (25005908).txt'):
    a, b = i.split(' ')
    a, b = int(a), int(b)
    data.append([a, b])
summa_v = 0
summa_n = 0
minim = 10000000
for i in data:
    summa_v += max(i)
    summa_n += min(i)
    if i[0] != i[1] and abs(i[0] - i[1]) < minim:
        minim = min(abs(i[0] - i[1]), minim)
        n = max(i)
        v = min(i)
print(summa_v - minim, summa_n - n + v)

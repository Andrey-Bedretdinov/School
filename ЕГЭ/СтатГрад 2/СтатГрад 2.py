from functools import lru_cache

print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if (((x <= y) and (z or w)) <= ((x == w) or (y and not z))) == 0:
                    print(x, y, z, w)

print('------------')


def f(s):
    s = s // 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s = s + 13
        n = n + 5
    return n


for i in range(100000, 0, -1):
    if f(i) == 121:
        print(i)
        break

print('------------')

count = 0
letters = 'СВЕТЛАН'
for a1 in letters:
    for a2 in letters:
        for a3 in letters:
            for a4 in letters:
                for a5 in letters:
                    for a6 in letters:
                        for a7 in letters:
                            for a8 in letters:
                                word = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
                                if 'АА' in word:
                                    continue
                                if all(word.count(x) == 1 for x in 'СВЕТЛН') and word.count('А') == 2:
                                    count += 1
print(count)

print('------------')


def f(s):
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    return s.count('1')


minim = 10000000000000000
count = 0
for i in range(1000, 199, -1):
    a = f('1' * i)
    if a > count:
        minim = i
        count = a
print(minim, count, f('1' * 204))


print('------------')

a = 2*216**8+4*36**12+6**15-1296
count = 0
while a != 0:
    if a % 6 == 0:
        count += 1
    a //= 6
print(count)

print('------------')


def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 2:
        return f(n - 1) + 1
    if n > 0 and n % 3 < 2:
        return f((n - n % 3) / 3)


for i in range(1000000000):
    if f(i) == 5:
        print(i)
        break


print('------------')

data = []
for i in open('17.txt'):
    data.append(int(i))

even = []
for i in data:
    if i % 2 == 0:
        even.append(i)
sr_ar = sum(even) / len(even)

count = 0
max_sum = 0
for i in range(len(data) - 1):
    if (data[i] % 3 == 0 or data[i + 1] % 3 == 0) and (data[i] < sr_ar or data[i + 1] < sr_ar):
        count += 1
        max_sum = max(max_sum, data[i] + data[i + 1])
print(count, max_sum)

print('------------')


def moves(p, last=''):
    if last == '':
        return p + 1, p + 2, p * 2
    if last == 1:
        return p + 2, p * 2
    if last == 2:
        return p + 1, p * 2
    if last == 3:
        return p + 2, p + 1


@lru_cache()
def f(p, last=''):
    if p >= 50:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p, last)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p, last)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p, last)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p, last)):
        return 'П2'
    if any(f(x) == 'П2' or f(x) == 'П1' for x in moves(p, last)):
        return 'В3'


'------------'


def f(x):
    a = 1
    b = 0
    while x > 0:
        d = x % 9
        a *= d
        if d < 5:
            b += d
        x //= 9
    return a, b


for i in range(10000000, 0, -1):
    if f(i) == (14, 8):
        print(i)
        break

print('------------')


def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start + 1, stop) + f(start * 3, stop)


print(f(1, 10) * f(10, 15))

print('------------')

file = open('24.txt')
data = file.read()
file.close()

max_count = 1
string = ''
for i in data:
    if i != 'E':
        string += i
    else:
        if string.count('A') >= 3:
            max_count = max(max_count, len(string))
        string = ''
print(max_count)

print('------------')


def f(n):
    n = str(n)
    sum_1 = 0
    for i in n:
        if int(i) % 2 == 0:
            sum_1 += int(i)
    sum_2 = 0
    for i in range(1, len(n), + 2):
        sum_2 += int(n[i])
    return abs(sum_1 - sum_2)


for i in range(1, 1000000000):
    if f(i) == 7:
        print(i)
        break

print('------------')


def get_divs(a):
    divs = set()
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            divs.add(i)
            divs.add(a // i)
    if len(divs) < 2:
        return []
    return list(divs)


k = 0
a = 11000001
while k != 5:
    divs = get_divs(a)
    if divs != [] and divs[-1] + divs[-2] < 10000:
        print(divs[0] + divs[1])
        k += 1
    a += 1


'''
1) 16
2) yxwz
3) 306100
4) 01010001
5) 17
6) 779
7) 960
8) 15120
9) 1878
10) 5
11) 13
12) 9991
13) 44
14) 14
15) 
16) 242
17) 2288 14875
18) 1825 -2328
19) 16 14 15 5
20) 34610095
21) 21824
22) 275
23) 4426 68484 45084 3624 3042
24)
25)
'''

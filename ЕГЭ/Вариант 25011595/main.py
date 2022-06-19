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














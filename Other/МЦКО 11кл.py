print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if (not (x * y)) * (y + z) + (not w) == 0:
                    print(x, y, z, w)

print('----------')


def f(s):
    n = 1
    while s < 45:
        s += 6
        n *= 4
    return n


for i in range(11111, 0, -1):
    if f(i) == 256:
        print(i)
        break

print('----------')

s = '3' * 250
while '3333' in s or '7777' in s:
    if '3333' in s:
        s = s.replace('3333', '7', 1)
    else:
        s = s.replace('777', '3', 1)
print(s)

print('----------')

count = 0
a = 64**9 + 8**25 - 9
while a != 0:
    if a % 8 == 7:
        count += 1
    a //= 8
print(count)

print('----------')


def f(x):
    l = 0
    m = 0
    while x > 0:
        m += 2
        if x % 8 != 0:
            l += 1
        x //= 8
    return l, m


for i in range(1000000000):
    if f(i) == (2, 6):
        print(i)
        break


print('----------')


for a in range(1, 10000):
    for x in range(1, 10000):
        if not (a % 34 == 0 and (238 % x != 0 or (a % x == 0 or 120 % x != 0))):
            break
    else:
        print(a)
        break

print('----------')

file = open('12.txt')
data = file.read()
file.close()
data = data.split('\n')
for i in range(len(data)):
    data[i] = int(data[i])
count = 0
sums = []
for i in range(1, len(data)):
    if data[i - 1] % 5 == 0 or data[i] % 5 == 0:
        count += 1
        sums.append(data[i - 1] + data[i])
print(count, min(sums))

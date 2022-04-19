print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if not (((w <= z) and ((not x) <= y)) <= ((y == w) or (z and (not x)))):
                    print(x, y, z, w)


def f(n):
    n = bin(n)[2:]
    n += n[-1]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    return int(n, 2)


minim = 100000000
for i in range(10000):
    ans = f(i)
    if ans > 114:
        minim = min(minim, ans)
print(minim)


s = '5' * 146
while '333' in s or '555' in s:
    if '555' in s:
        s = s.replace('555', '3', 1)
    else:
        s = s.replace('333', '5', 1)
print(s)


def f(start, stop):
    if start > stop or start == 12:
        return 0
    elif start == stop:
        return 1
    return f(start + 1, stop) + f(start * 2, stop)


print(f(3, 20) * f(20, 30))




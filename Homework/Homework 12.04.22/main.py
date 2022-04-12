# Number 1
number = 8 ** 1341 - 4 ** 1342 + 2 ** 1343 - 1344
number = bin(number)[2:]
print(number.count('1'))

# Number 3
print('x y z')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            if (((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))) == 1:
                print(x, y, z)

# Number 4
count = 0
chars = 'ПИРОГ'
for a1 in chars:
    if a1 == 'О':
        continue
    for a2 in chars:
        for a3 in chars:
            for a4 in chars:
                word = a1 + a2 + a3 + a4
                if word.count('0') > 2:
                    continue
                for i in range(1, len(word)):
                    if word[i] == 'О' and word[i - 1] in 'ИО':
                        break
                else:
                    count += 1

print(count)

# Number 5
def f(x):
    l = 0
    m = 0
    while x > 0:
        m += 1
        if x % 2 != 0:
            l += 1
        x //= 2
    return l, m


for i in range(10000, 0, -1):
    if f(i) == (5, 8):
        print(i)
        break

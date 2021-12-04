# Number 1
def f1(s):
    n = 200
    while s // n >= 2:
        s += 5
        n += 5
    return s


for i in range(1000, 0, -1):
    if len(str(f1(i))) == 3:
        print('\nNumber 1:', i)
        break

'--------------------------------------------'

# Number 2
print('Number 2: 20')

'--------------------------------------------'

# Number 3
print('Number 3: 21')

'--------------------------------------------'

# Number 4
s = '123' * 50
while '13' in s or '32' in s or '12' in s:
    if '13' in s:
        s = s.replace('13', '31', 1)
    if '32' in s:
        s = s.replace('32', '23', 1)
    if '12' in s:
        s = s.replace('12', '21', 1)
print('Number 4:', s[10], s[70], s[140])

'--------------------------------------------'

# Number 5
numbers = []
for i in range(1206, 14993 + 1):
    if (i % 10) in [3, 6] and i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
        numbers.append(i)
print('Number 5:', len(numbers), min(numbers))

'--------------------------------------------'


# Number 6
def f6(x):
    l = x - 15
    m = x + 20
    while l != m:
        if l > m:
            l -= m
        else:
            m -= l
    return m


for i in range(101, 100000000):
    if f6(i) == 35:
        print('Number 6:', i)
        break

# Number 1
def f(s):
    n = 100
    while s - n >= 100:
        s += 20
        n += 40
    return s


for i in range(1000000):
    if f(i) != i:
        print('\nNumber 1:', i)
        break

'------------------------------------'

# Number 2
print('Number 2: 24')

'------------------------------------'

# Number 3
print('Number 3: 15')

'------------------------------------'

# Number 4
s = '>' + '3' * 10 + '2' * 17 + '1' * 25
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>3', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '11>2', 1)
summa = 0
for i in s:
    if i != '>':
        summa += int(i)
print('Number 4:', summa)

'------------------------------------'

# Number 5
count = 0
maximum = -10000
numbers = []
for i in open('17-1.txt'):
    numbers.append(int(i))
for i in range(1, len(numbers) - 1):
    if (numbers[i] % 9 == 0 and numbers[i + 1] % 8 == 3) or \
            (numbers[i + 1] % 9 == 0 and numbers[i] % 8 == 3):
        count += 1
        if maximum < max(numbers[i], numbers[i + 1]):
            maximum = max(numbers[i], numbers[i + 1])
print('Number 5:', count, maximum)

'------------------------------------'


# Number 6
def f(x):
    l = 0
    m = 0
    while x > 0:
        l += 1
        if m < x and x % 2 == 0:
            m = x % 10
        x //= 10
    return l, m


for i in range(10000, 0, -1):
    if f(i)[0] == 3 and f(i)[1] == 8:
        print('Number 6:', i)
        break


'''
    Number 1: 200
    Number 2: 24
    Number 3: 15
    Number 4: 274
    Number 5: 275 9971
    Number 6: 998
'''

# Number 1
def f(d):
    s = 5
    n = 7
    while s <= 3011:
        s += d
        n += 124
    return n


count = 0
for i in range(8, 100000, 10):
    if f(i) == 1247:
        count += 1
print('#1:', count)

'-----------------------------'

# Number 2
print('#2: 16')

'-----------------------------'

# Number 3
print('#3: 5')

'-----------------------------'


# Number 4
def f(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    return s


string = '1' * 50
for i in range(10000000):
    if f(string + '1' * i) == '22':
        print('#4:', (string + '1' * i).count('1'))
        break

'-----------------------------'


# Number 5
def f(n):
    summ = n**2
    if n > 1:
        summ += (2 * n + 1) + f(n - 2) + f(n // 3)
    return summ


for i in range(10000000000000):
    if f(i) > 3200000:
        print('#5:', i, f(i))
        break

'-----------------------------'

# Number 6
numbers = []
for i in open('17-2.txt'):
    numbers.append(int(i))
maxim = max(numbers)
count = numbers.count(maxim)
print('#6:', count, numbers.index(maxim) + 1)

'-----------------------------'


# Number 7
def f(x):
    a = 0
    b = 10
    while x > 0:
        c = x % 10
        a += c
        if c < b:
            b = c
        x //= 10
    return a, b


for i in range(100000000):
    if f(i) == (14, 6):
        print('#7:', i)
        break

'-----------------------------'


# Number 8
def f(start, stop):
    if start > stop or start == 15:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start + 3, stop)


print('#8:', f(2, 10) * f(10, 20))

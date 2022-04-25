'''def f(x):
    s = 6 * (x // 15)
    n = 1
    while s < 300:
        s += 18
        n *= 2
    return n


count = 0
for x in range(10000):
    if 2 <= f(x) <= 500:
        count += 1
print(count)


def f(count5):
    s = '5' * count5
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    return s.count('5'), s.count('8')


for i in range(301, 10000):
    ans = f(i)
    if ans[0] > ans[1]:
        print(i)
        break


def f(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return 11 * n + f(n - 1)
    else:
        return 11 * f(n - 2) + n


summ = 0
for i in range(35, 51):
    ans = f(i)
    if ans % 2 == 0:
        summ += ans

number = 0
while summ != 0:
    summ //= 10
    number += 1
print(number)


with open('17-3.txt') as file:
    data = []
    for line in file:
        data.append(int(line))

summ = 0
count = 0
for i in range(len(data) - 2):
    numbers = [data[i], data[i + 1], data[i + 2]]
    if sum(numbers) < max(numbers):
        count += 1
        summ += max(numbers) + min(numbers)
print(count, summ)


with open('24-3.txt') as file:
    data = file.read()

s = ''
count = 0
for char in data:
    if char == 'A':
        s = 'A'
    elif char == 'B' and s != '' and s.count('F') == 2:
        count += 1
        s = ''
    elif s:
        s += char
print(count)


def f(start, stop):
    if start > stop or start == 21:
        return 0
    if start == stop:
        return 1
    if start % 2 == 0:
        number = start + 2
    else:
        number = start + 1
    return f(start + 1, stop) + f(start + 4, stop) + f(start + number, stop)


print(f(2, 11) * f(11, 26))'''


def f(x):
    a = 5
    b = 20
    while x > 0:
        d = x % 6
        a *= d
        if d < 3:
            b += d
        x //= 6
    return a, b


for i in range(100000000, 0, -1):
    if f(i) == (30, 31):
        print(i)
        break




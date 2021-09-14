from random import random

# 1
print('#1')
a = int(input())
a1 = a // 1000000
a2 = a // 1000 % 1000
a3 = a // 100 % 10
a4 = a // 10 % 10
a5 = a % 10
print(a1, a2, a3, a4, a5)


# 2
print('\n------------\n\n#2')
a = int(input())
if 11 <= a % 100 <= 14 or a % 10 == 0 or a % 10 > 4:
    print(a, 'лет')
elif a % 10 == 1:
    print(a, 'год')
else:
    print(a, 'года')


# 3
print('\n------------\n\n#3')
p = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
     10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
     16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
     40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
a = int(input())
if a == 100:
    print('100')
else:
    a0 = a % 10
    a1 = a // 10 * 10
    print(a, '- "{} {}"'.format(p[a1], p[a0]))


# 4
def f(n):
    k1, k2, k3, k4 = [], [], [], []
    for i in range(1, n+1):
        a = random()
        if a < 0.25:
            k1.append(a)
        elif a < 0.5:
            k2.append(a)
        elif a < 0.75:
            k3.append(a)
        elif a < 1:
            k4.append(a)
    print('[0, 0.25) - {} числел'.format(len(k1)))
    print('[0.25, 0.5) - {} чисел'.format(len(k2)))
    print('[0.5, 0.75) - {} чисел'.format(len(k3)))
    print('[0.75, 1) - {} чисел'.format(len(k4)))
    print('{}\n{}\n{}\n{}'.format(k1, k1, k3, k4))


print('\n------------\n\n#4')
f(int(input()))


# 5
print('\n------------\n\n#5')
k1, k2 = [], []
for i in range(10000, 100000):
    if i % 133 == 125:
        k1.append(i)
    if i % 134 == 111:
        k2.append(i)
print('При делении на 133 остаток 125 - {} чисел:\n{}'.format(len(k1), k1))
print('При делении на 134 остаток 111 - {} чисел:\n{}'.format(len(k2), k2))


# 6
print('\n------------\n\n#6')
a = str(input())
x = int(input())
r = []
for i in a:
    r.append(i)
r.reverse()
while a == 0:
    pass
print(r)

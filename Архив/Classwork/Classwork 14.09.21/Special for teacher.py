from random import random

# 1
print('#1')
a = int(input('Введите число от миллиона: '))
a1 = a // 1000000
a2 = a // 1000 % 1000
a3 = a // 100 % 10
a4 = a // 10 % 10
a5 = a % 10
print(f'Миллионов - {a1}\nТысяч - {a2}\nСотен - {a3}\nДесятков - {a4}\nЕдиниц - {a5}')

# 2
print('\n-------------------------------\n')
print('#2')
a = int(input('Введите возраст: '))
if 11 <= a % 100 <= 14 or a % 10 == 0 or a % 10 > 4:
    print(a, 'лет')
elif a % 10 == 1:
    print(a, 'год')
else:
    print(a, 'года')

# 3
print('\n-------------------------------\n')
print('#3')
p = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
     10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
     16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
     40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
a = int(input('Введите число: '))
if a == 100:
    print('сто')
else:
    a0 = a % 10
    a1 = a // 10 * 10
    print(a, '- "{} {}"'.format(p[a1], p[a0]))

# 4
print('\n-------------------------------\n')
print('#4')


def f(n):
    k1, k2, k3, k4 = [], [], [], []
    for i in range(1, n + 1):
        a = random() // 0.01 / 100
        if a < 0.25:
            k1.append(a)
        elif a < 0.5:
            k2.append(a)
        elif a < 0.75:
            k3.append(a)
        elif a <= 1:
            k4.append(a)
    print('[0, 0.25) - {} числел'.format(len(k1)))
    print('[0.25, 0.5) - {} чисел'.format(len(k2)))
    print('[0.5, 0.75) - {} чисел'.format(len(k3)))
    print('[0.75, 1) - {} чисел'.format(len(k4)))
    print('\n{}\n{}\n{}\n{}'.format(k1, k1, k3, k4))


f(int(input('Введите количество чисел: ')))

# 5
print('\n-------------------------------\n')
print('#5')
k1, k2 = [], []
for i in range(10000, 100000):
    if i % 133 == 125:
        k1.append(i)
    if i % 134 == 111:
        k2.append(i)
print('\nПри делении на 133 остаток 125 - {} чисел:\n{}'.format(len(k1), k1))
print('\nПри делении на 134 остаток 111 - {} чисел:\n{}'.format(len(k2), k2))

# 6
print('\n-------------------------------\n')
print('#6')
a = int(input('Введите число: '))
x = int(input('Введите конечную СС: '))
k = ''
while a != 0:
    k = str(a % x) + k
    a //= x
print('Ответ: ', k)

# 7
print('\n-------------------------------\n')
print('#7')


def f7(x_):
    r_ = []
    x_ = str(x_)
    for i_ in x_:
        r_.append(int(i_))
    if 0 in r_:
        return False
    x_ = int(x_)
    for div in r_:
        if x_ % div == 0:
            continue
        return False
    return True


a = int(input('Введите натуральное число: '))
numbers = []
for i in range(a + 1):
    if f7(i):
        numbers.append(i)
print(numbers)

# 8
print('\n-------------------------------\n')
print('#8')
numbers = []
for i in range(100, 10000):
    r = []
    x = str(i)
    for digit in x:
        r.append(int(digit))
    k = 0
    for elem in r:
        r[k] = elem ** len(r)
        k += 1
    if sum(r) == i:
        numbers.append(str(i))
print('Числа Армстронга:', ', '.join(numbers))

# 9
print('\n-------------------------------\n')
print('#9')
n = int(input('Введите натуральное число: '))
numbers = []
for i in range(n + 1):
    i_ = str(i ** 2)
    if i_[-len(str(i)):] == str(i):
        numbers.append(i)
print(numbers)

# 10
print('\n-------------------------------\n')
print('#10')
a = int(input('Введите число: '))
k = 0
while a != 0:
    if a % 2 == 0:
        k += 1
    a //= 10
print('Количество четных цифр -', k)

# 11
print('\n-------------------------------\n')
print('#11')
a = int(input('Введите число: '))
summa = 0
while a != 0:
    summa += a % 10
    a //= 10
print('Сумма всех цифр -', summa)

# 12
print('\n-------------------------------\n')
print('#12')
a = int(input('Введите число: '))
i = -1
while a != 0:
    k = a % 10
    if k != i:
        i = k
        a //= 10
    else:
        print('Число содержит одинаковые цифры, стоящие рядом')
        break
else:
    print('Число не содержит одинаковых цифр, стоящих рядом')

# 13
print('\n-------------------------------\n')
print('#13')
a = int(input('Введите число: '))
i = a % 10
while a != 0:
    k = a % 10
    if k != i:
        print('Не все цифры одинаковые')
        break
    a //= 10
else:
    print('Все цифры одинаковые')

# 14
print('\n-------------------------------\n')
print('#14')
a = list(str(input('Введите число: ')))
for number in range(10):
    number = str(number)
    k = 0
    for i in a:
        if k < 2:
            if number == i:
                k += 1
        if k == 2:
            print('В числе есть одинаковые цифры')
            break
    else:
        continue
    break
else:
    print('В числе нет одинаковых цифр')

# 15
print('\n-------------------------------\n')
print('#15')
a1 = int(input('Введите первое число: '))
a2 = int(input('Введите второе число: '))
while a1 != 0 and a2 != 0:
    if a1 < a2:
        a2 -= a1
    else:
        a1 -= a2
if a1 != 0:
    print(a1, '- наибольший общий делитель')
else:
    print(a2, '- наибольший общий делитель')

# 16
print('\n-------------------------------\n')
print('#16')
a1 = int(input('Введите первое число: '))
a2 = int(input('Введите второе число: '))
while a1 != 0 and a2 != 0:
    if a1 < a2:
        a2 %= a1
    else:
        a1 %= a2
if a1 != 0:
    print(a1, '- наибольший общий делитель')
else:
    print(a2, '- наибольший общий делитель')

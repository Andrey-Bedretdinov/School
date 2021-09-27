# 1
print('\n----------------------\n\n# 1')
minim = 7564
k = 0
for i in range(1056, 7564):
    if (i % 3 == 0 or i % 11 == 0) and i % 13 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0:
        if minim > i:
            minim = i
        k += 1
print(f'Количество - {k}\nМинимальное - {minim}')


# 2
print('\n----------------------\n\n# 2')


def ss(a, x):
    ans = ''
    while a != 0:
        remainder = a % x
        if remainder == 10:
            remainder = 'A'
        elif remainder == 11:
            remainder = 'B'
        elif remainder == 12:
            remainder = 'C'
        elif remainder == 13:
            remainder = 'D'
        elif remainder == 14:
            remainder = 'E'
        elif remainder == 15:
            remainder = 'F'
        ans = str(remainder) + ans
        a //= x
    return ans


maxim = 0
k = 0
for i in range(1000, 70001):
    if len(ss(i, 8)) == 5 and len(ss(i, 5)) == 6 and ss(i, 16)[-2:] == 'FA':
        if maxim < i:
            maxim = i
        k += 1
print(f'Количество - {k}\nМаксимальное - {maxim}')


# 3
print('\n----------------------\n\n# 3')
summ = 0
minim = 1178
for i in range(10, 1179, 2):
    i = str(i)
    if i[-1] != '0' and i[-1] != '2' and i[-1] != '6' and i[-1] != '8' and i[:-2] != '14':
        i = int(i)
        if minim > i:
            minim = i
        summ += i
print(f'Сумма чисел - {summ}\nМинимальное - {minim}')

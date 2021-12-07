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

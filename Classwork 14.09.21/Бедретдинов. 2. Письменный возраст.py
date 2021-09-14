a = int(input('Введите возраст: '))
if 11 <= a % 100 <= 14 or a % 10 == 0 or a % 10 > 4:
    print(a, 'лет')
elif a % 10 == 1:
    print(a, 'год')
else:
    print(a, 'года')
a = int(input('Введите число: '))
summa = 0
while a != 0:
    summa += a % 10
    a //= 10
print('Сумма всех цифр -', summa)

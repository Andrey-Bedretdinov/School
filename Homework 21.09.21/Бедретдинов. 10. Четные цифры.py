a = int(input('Введите число: '))
k = 0
while a != 0:
    if a % 2 == 0:
        k += 1
    a //= 10
print('Количество четных цифр -', k)

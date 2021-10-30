a = int(input('\nВведите число: '))
x = int(input('Введите конечную СС: '))

answer = ''
while a != 0:
    number = a % x
    if number == 10:
        number = 'A'
    elif number == 11:
        number = 'B'
    elif number == 12:
        number = 'C'
    elif number == 13:
        number = 'D'
    elif number == 14:
        number = 'E'
    elif number == 15:
        number = 'F'

    answer = str(number) + answer
    a //= x
print(f'\nЧисло в {x} СС - {answer}')

k = 0
for i in range(0, 10):
    i = str(i)
    for number in answer:
        if number == i:
            k += 1
            break
print(f'Различных цифр - {k}')

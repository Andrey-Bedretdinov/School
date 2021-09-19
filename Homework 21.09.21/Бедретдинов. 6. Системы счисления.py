a = int(input('\nВведите число: '))
x = int(input('Введите конечную СС: '))

answer = ''
while a != 0:
    answer = str(a % x) + answer
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

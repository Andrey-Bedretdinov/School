print('\n-------------------------------\n')
print('#6')
a = int(input('Введите число: '))
x = int(input('Введите конечную СС: '))
k = ''
while a != 0:
    k = str(a % x) + k
    a //= x
print('Ответ: ', k)
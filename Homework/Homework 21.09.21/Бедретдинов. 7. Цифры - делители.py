a = int(input('Введите число: '))
for number in range(a + 1):
    for i in str(number):
        if i == '0':
            break
        if number % int(i) == 0:
            continue
        break
    else:
        print(number)

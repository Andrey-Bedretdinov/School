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

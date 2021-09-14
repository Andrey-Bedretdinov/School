def numbers(x):
    n = len(x) - 1
    while n >= 0:
        print(x[n])
        n -= 1


number = input('Введите число: ')
numbers(number)

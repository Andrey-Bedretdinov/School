from random import random


def f(n):
    k1, k2, k3, k4 = [], [], [], []
    for i in range(1, n+1):
        a = random() // 0.01 / 100
        if a < 0.25:
            k1.append(a)
        elif a < 0.5:
            k2.append(a)
        elif a < 0.75:
            k3.append(a)
        elif a <= 1:
            k4.append(a)
    print('[0, 0.25) - {} числел'.format(len(k1)))
    print('[0.25, 0.5) - {} чисел'.format(len(k2)))
    print('[0.5, 0.75) - {} чисел'.format(len(k3)))
    print('[0.75, 1) - {} чисел'.format(len(k4)))
    print('\n{}\n{}\n{}\n{}'.format(k1, k1, k3, k4))


f(int(input('Введите количество чисел: ')))

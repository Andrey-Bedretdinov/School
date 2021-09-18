from random import random


def f(n):
    k1, k2, k3, k4 = 0, 0, 0, 0
    for i in range(1, n+1):
        a = random() // 0.01 / 100
        if a < 0.25:
            k1 += 1
        elif a < 0.5:
            k2 += 1
        elif a < 0.75:
            k3 += 1
        elif a <= 1:
            k4 += 1
    print('[0, 0.25) - {} числел'.format(k1))
    print('[0.25, 0.5) - {} чисел'.format(k2))
    print('[0.5, 0.75) - {} чисел'.format(k3))
    print('[0.75, 1) - {} чисел'.format(k4))


f(int(input('Введите количество чисел: ')))

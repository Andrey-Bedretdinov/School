from math import atan, pi
import numexpr as ne


def get_rf(a, b):
    r = round((a**2 + b**2)**0.5, 2)
    f = round(atan(b/a)*180/pi)
    return r, f


while True:
    a = ne.evaluate(input('Введи действительное число: '))
    b = ne.evaluate(input('Введи мнимое число: '))
    r, f = get_rf(a, b)
    print(f'r = {r}, f = {f}°\n')

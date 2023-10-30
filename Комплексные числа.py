from math import atan, pi, cos, sin
import numexpr as ne


def get_rf(a, b):
    r = round((a**2 + b**2)**0.5, 2)
    f = round(atan(b/a), 2)
    return r, f


while True:
    a = ne.evaluate(input('Введи действительную часть числа: '))
    b = ne.evaluate(input('Введи мнимую часть числа: '))
    n = int(input('Введи степень числа: '))
    m = int(input('Введи корень числа: '))
    r, f = get_rf(a, b)
    print(f'\nr = {r}, f = {f} ({round(f*180/pi, 2)}°)\n')

    f = atan(b/a)
    s = [round(abs(r**n) * cos(n * f), 2), round(abs(r**n) * sin(n * f), 2)]
    print(f'Число в степени {n}: {s[0]} + {s[1]}*i')

    for i in range(m):
        k = ([round(abs(r**(1/m)) * cos((f + 2*pi*i) / m), 2), round(abs(r**(1/m)) * sin((f + 2*pi*i) / m), 2)])
        print(f'Корень ({m}) #{i+1}: {k[0]} + {k[1]}*i')
    print('-------------\n')

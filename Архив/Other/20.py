def f(x):
    a = 7 * x + 27
    b = 7 * x - 33
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        'print(x)'
    return a


for i in range(10, 10000000):
    if f(i) == 15:
        print(i)
        break

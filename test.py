import alive_progress


def f(x):
    a = 5
    b = 20
    while x > 0:
        d = x % 6
        a *= d
        if d < 3:
            b += d
        x //= 6
    return a, b


with alive_progress.alive_bar(100000000) as bar:
    for i in range(100000000, 0, -1):
        bar()
        if f(i) == (30, 31):
            print(i)
            break
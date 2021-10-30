def f(x, stop):
    if x > stop:
        return 0
    elif x == stop:
        return 1
    else:
        return f(x + 1, stop) + f(x * 3, stop)


print(f(2, 26) * f(26, 87))
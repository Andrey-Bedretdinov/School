def f(n):
    if n <= 10:
        return n
    elif n <= 36:
        return n // 4 + f(n - 10)
    else:
        return 2 * f(n - 5)


print(f(100))

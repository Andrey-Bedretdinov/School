def f(n):
    if n > 12:
        return 2 * n - 5
    else:
        return 2 * f(n + 2) + n - 4


print(f(1))

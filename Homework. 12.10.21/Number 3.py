# Способ 1
def f(n):
    if n < 1:
        return 1
    elif n % 2 == 0:
        return n + 3 * f(n - 3)
    else:
        return 5 * n + 2 * f(n - 5)


print(f(30))

# Способ 2

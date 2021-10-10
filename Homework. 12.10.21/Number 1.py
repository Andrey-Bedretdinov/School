def f(n):
    k = 1
    if n >= 1:
        k += 1 + f(n - 1) + f(n - 2) + 1
    return k


print(f(35))

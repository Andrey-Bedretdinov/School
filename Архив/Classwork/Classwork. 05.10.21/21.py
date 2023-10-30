def f(n):
    count = 1
    if n >= 1:
        count += 1 + f(n - 1) + f(n - 2)
    return count


print(f(28))

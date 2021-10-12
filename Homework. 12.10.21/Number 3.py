# Способ 1
def f(n):
    if n < 1:
        return n
    elif n % 2 == 0:
        return n + 3 * f(n - 3)
    return 5 * n + 2 * f(n - 5)


print(f(30))

# Способ 2
F = [1] * 31
for i in range(1, 31):
    if i < 1:
        F[i] = 1
    elif i % 2 == 0:
        if i < 3:
            F[i] = i + 3 * (i - 3)
        else:
            F[i] = i + 3 * F[i - 3]
    else:
        if i < 5:
            F[i] = 5 * i + 2 * (i - 5)
        else:
            F[i] = 5 * i + 2 * F[i - 5]
print(F[30])

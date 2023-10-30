def f(n):
    if n < 3:
        return 2 * n
    elif n % 2 == 0:
        return 3 * n + 5 + f(n - 2)
    return n + 2 * f(n - 6)


print(f(61))


F = [1] * 62
for i in range(1, 62):
    if i < 3:
        F[i] = 2 * i
    elif i % 2 == 0:
        if i < 2:
            F[i] = 3 * i + 5 + (i - 2)
        else:
            F[i] = 3 * i + 5 + F[i - 2]
    else:
        if i < 6:
            F[i] = i + 2 * (i - 6)
        else:
            F[i] = i + 2 * F[i - 6]
print(F[61])

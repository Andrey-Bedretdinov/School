def f(n):
    if n <= 10:
        return n
    elif n <= 36:
        return n // 4 + f(n - 10)
    else:
        return 2 * f(n - 5)


print(f(100))

F = [0] * 101
for i in range(101):
    if i <= 10:
        F[i] = i
    elif i <= 36:
        F[i] = i // 4 + F[i - 10]
    else:
        F[i] = 2 * F[i - 5]
print(F[100])

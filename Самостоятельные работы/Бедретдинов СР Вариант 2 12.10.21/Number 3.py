def f(n):
    count = 1
    if n >= 1:
        count += 1 + f(n - 1) + f(n // 3) + 1
    return count


print(f(280))


F = [1] * 281
for i in range(1, 281):
    F[i] = 2 + F[i - 1] + F[i // 3] + 1
print(F[280])

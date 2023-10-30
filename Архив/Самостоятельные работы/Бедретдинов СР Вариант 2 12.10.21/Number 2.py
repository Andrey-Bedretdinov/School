def f(n):
    if n == 1:
        return 1
    return 2 * f(n - 1) + g(n - 1) - 2 * n


def g(n):
    if n == 1:
        return 1
    return f(n - 1) + 2 * g(n - 1) + n


print(f(14) + g(14))


F = [1, 1]
G = [1, 1]
for i in range(2, 15):
    F.append(2 * F[i - 1] + G[i - 1] - 2 * i)
    G.append(F[i - 1] + 2 * G[i - 1] + i)
print(F[14] + G[14])

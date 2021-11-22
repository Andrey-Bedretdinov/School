# Способ 1
def f(n):
    if n == 1:
        return 1
    return 3 * f(n - 1) + g(n - 1) - n + 5


def g(n):
    if n == 1:
        return 1
    return f(n - 1) + 3 * g(n - 1) - 3 * n


print(f(14) + g(14))

# Способ 2
F = [0, 1]
G = [0, 1]
for i in range(2, 15):
    F.append(3 * F[i - 1] + G[i - 1] - i + 5)
    G.append(F[i - 1] + 3 * G[i - 1] - 3 * i)
print(F[14] + G[14])

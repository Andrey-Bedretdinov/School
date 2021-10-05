def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) - 2 * g(n - 1)


def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + 2 * g(n - 1)


print(g(21))

F = [0, 1]
G = [0, 1]
for i in range(2, 22):
    F.append(F[i - 1] - 2 * G[i - 1])
    G.append(F[i - 1] + 2 * G[i - 1])
print(G[21])

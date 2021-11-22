# Способ 1
def f(n):
    if n > 25:
        return 2 * n**3 + 1
    return f(n + 2) + 2 * f(n + 3)


count = 0
for i in range(1001):
    if f(i) % 11 == 0:
        count += 1
print(count)

# Способ 2

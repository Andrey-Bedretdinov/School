def f(n):
    if n <= 15:
        return n * n + 11
    elif n % 2 == 0 and n > 15:
        return f(n // 2) + n * n * n - 5 * n
    else:
        return f(n + 1) + 2 * n + 3


count = 0
for i in range(1, 1001):
    res = f(i)
    if str(res).count('6') >= 3:
        count += 1
print(count)

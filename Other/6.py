def f(s):
    s = 3 * (s // 10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    return n


k = 0
for i in range(100000):
    if f(i) == 256:
        k += 1
print(k)
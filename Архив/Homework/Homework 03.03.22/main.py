'''def f(n):
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return div + n // div
    return 0


k = 0
for i in range(452021, 100000000):
    if f(i) % 7 == 3:
        print(i, f(i))
        k += 1
    if k >= 5:
        break'''


def is_simple(n):
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    return True


for i in range(45000000, 50000001):
    if i**0.5 % 1 != 0:
        continue
    div = i
    while div % 2 == 0:
        div //= 2
    if div == i**0.25 and div**2 == i**0.5 and div**3 == i**0.75 and div**4 == i:
        print(i)

def SumDigit(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


def SortSumDigit(a):
    for j in range(len(a) - 1):
        for i in range(len(a) - 1 - j):
            if SumDigit(a[i]) > SumDigit(a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]


f = open('test.txt', encoding='UTF8')
Numbers = f.read().split()
f.close()
for i in range(len(Numbers)):
    Numbers[i] = int(Numbers[i])
print(Numbers)
SortSumDigit(Numbers)
print(Numbers)

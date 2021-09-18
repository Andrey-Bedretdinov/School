numbers = []
for i in range(100, 10000):
    r = []
    x = str(i)
    for digit in x:
        r.append(int(digit))
    k = 0
    for elem in r:
        r[k] = elem**len(r)
        k += 1
    if sum(r) == i:
        numbers.append(str(i))
print('Числа Армстронга:', ', '.join(numbers))

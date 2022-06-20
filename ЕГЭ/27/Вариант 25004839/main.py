with open('27_A.txt') as file:
    n = int(file.readline())
    data = [int(file.readline()) for _ in range(n)]

summ = 0  # текущая сумма
min_sum = [10**20] * 45  # минимальные суммы по остатку
min_len = [0] * 45  # минимальные длины по остатку
ms = 0  # локальная максимальная сумма
MS = 0  # глобальная максимальная сумма
ml = 10**20  # локальная минимальная длина
ML = 10**20  # глобальная минимальная длина
for i in range(len(data)):
    a = data[i]
    summ += a
    ost = summ % 43
    if ost == 0:
        MS = summ
        ML = i
    else:
        ms = summ - min_sum[ost]
        ml = i - min_len[ost]
        if ms > MS:
            MS = ms
            ML = ml
        elif ms == MS:
            ML = min(ML, ml)
    if summ < min_sum[ost]:
        min_sum[ost] = summ
        min_len[ost] = i

print(ML)




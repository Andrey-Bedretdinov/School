# Number 27
with open('27_B.txt') as file:
    n = int(file.readline())
    min_sum = [100000000000] * 43
    min_len = [0] * 43
    summa, MAX_SUM, MIN_LN, max_sum, ln = 0, 0, 0, 0, 0
    for i in range(n):
        a = int(file.readline())
        summa += a
        ost = summa % 43
        if ost == 0:
            MAX_SUM = summa
            MIN_LN = i
        else:
            max_sum = summa - min_sum[ost]
            ln = i - min_len[ost]
            if max_sum > MAX_SUM or (max_sum == MAX_SUM and ln < MIN_LN):
                MAX_SUM = max_sum
                MIN_LN = ln
        if summa < min_sum[ost]:
            min_sum[ost] = summa
            min_len[ost] = i
print(MIN_LN)





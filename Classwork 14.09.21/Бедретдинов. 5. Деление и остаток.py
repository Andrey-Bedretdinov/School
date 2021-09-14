k1, k2 = [], []
for i in range(10000, 100000):
    if i % 133 == 125:
        k1.append(i)
    if i % 134 == 111:
        k2.append(i)
print('\nПри делении на 133 остаток 125 - {} чисел:\n{}'.format(len(k1), k1))
print('\nПри делении на 134 остаток 111 - {} чисел:\n{}'.format(len(k2), k2))

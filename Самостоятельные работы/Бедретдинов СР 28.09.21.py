# Вариант 2
# 1
count = 0
minimal = 100000
for i in range(1305, 7851):
    if (i % 4 == 0 or i % 7 == 0) and i % 11 != 0 and i % 17 != 0 and i % 19 != 0 and i % 21 != 0:
        count += 1
        if i < minimal:
            minimal = i
print(count, minimal)

print('-----------')

# 2
count = 0
maximal = 0
for i in range(1156, 12210):
    if (i % 2 == 0 or i % 5 == 0) and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
        count += 1
        if i > maximal:
            maximal = i
print(count, maximal)

print('-----------')

# 3
minimal = 1000000
summa = 0
for i in range(1529, 9483):
    i1_2 = i % 3
    i2_2 = i // 3 % 3
    i1_5 = i % 5
    if i1_2 == 1 and i2_2 == 0 and i1_5 == 3:
        if minimal > i:
            minimal = i
        summa += i
print(minimal, summa)

print('-----------')

# 4
count = 0
minimal = 10000000
maximal = 0
for i in range(1476, 7040):
    if i % 2 == 0 and i % 16 != 0 and i // 10 % 10 >= 4:
        count += 1
        if minimal > i:
            minimal = i
        if maximal < i:
            maximal = i
print(count, int((minimal + maximal) / 2))

print('-----------')

# 5
count = 0
maximal = 0
for i in range(2848, 109500):
    k = False
    i_ = i
    summa = 0
    while i_ != 0:
        if i_ % 10 == 9:
            k = True
        if i_ % 10 > 5:
            summa += i_ % 10
        i_ //= 10
    if k and summa % 3 == 0:
        count += 1
        i_ = i
        while i_ != 0:
            if i_ // 10 == 0:
                break
            i_ //= 10
        if i_ == 8 and maximal < i:
            maximal = i
print(count, maximal)

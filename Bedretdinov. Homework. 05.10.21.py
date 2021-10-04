# 1
print('')
count = 0
minimum = 100000
for i in range(3712, 8433):
    if i % 2 == i % 4 and (i % 13 == 0 or i % 14 == 0 or i % 15 == 0):
        count += 1
        if i < minimum:
            minimum = i
print("#1 ", count, minimum)

# 2
minimum = 10000000
summa = 0
for i in range(1529, 9483):
    i21 = i % 2
    i22 = i // 2 % 2
    i51 = i % 5
    if i21 == 1 and i22 == 0 and i51 == 3:
        if i < minimum:
            minimum = i
        summa += i
print('#2 ', minimum, summa)

# 3
count = 0
maximum = 0
for i in range(1000, 10000):
    count6 = 0
    i_ = i
    while i_ != 0:
        count6 += 1
        i_ //= 6
    if count6 <= 5 and ((i % 5 == 3 or i % 5 == 4) and i // 5 % 5 == 1):
        count += 1
        if i > maximum:
            maximum = i
print('#3 ', count, maximum)

# 4
count = 0
maximum = 0
for i in range(3466, 9082):
    count8 = 0
    count10 = 0
    i_ = i
    while i_ != 0:
        count8 += 1
        i_ //= 8
    i_ = i
    while i_ != 0:
        count10 += 1
        i_ //= 10
    if count8 != count10 and (i % 7 == 1 or i % 7 == 5):
        count += 1
        if i > maximum:
            maximum = i
print('#4 ', count, maximum)

# 5
count = 0
maximum = 0
for i in range(117649, 823543):
    if i % 3 == 2 and i % 8 != 3 and i % 12 != 5:
        count += 1
        if i > maximum:
            maximum = i
print('#5 ', count, maximum)

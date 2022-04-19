def delete(a, b):
    if a % b == 0:
        return 1
    return 0

'''
for a in range(10000, 0, -1):
    for x in range(1, 10000):
        if not ((delete(x, 16) == delete(x, 24)) + delete(x, a)):
            break
    else:
        print(a)
        break

count = 0
for a in range(10000, 0, -1):
    for x in range(1, 1000):
        if not (delete(a, 5) * (not ((not delete(2020, a)) + delete(x, 1718)) + delete(2023, a))):
            break
    else:
        count += 1
print(count)

q = [x for x in range(29, 48)]
for a in range(1, 1000):
    for x in range(1, 1000):
        if not ((not delete(x, 3) and (x != 48 and x != 52 and x != 56)) <= (((-7 <= x - 50 <= 7) <= (x in q)) + (x & a == 0))):
            break
    else:
        print(a)
        break'''

for a in range(43, 56):
    for x in range(1, 1000):
        if ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0)):
            break
    else:
        print(a)
        break
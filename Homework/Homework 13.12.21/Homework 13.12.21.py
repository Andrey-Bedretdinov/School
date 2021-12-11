def f(a):
    a = bin(a)[2:]
    a = a + str(a.count('1') % 2)
    a = a + str(a.count('1') % 2)
    return int(a, 2)


for i in range(10000, 0, -1):
    if f(i) < 50:
        print('#2:', f(i))
        break

'---------------------------------'

dpi1 = 300
i1 = 16
I1 = 18
dpi2 = 200
i2 = 8
I2 = I1 // 9 // 2
print('#4:', I2)

'---------------------------------'

count = 0
letters = 'РАЗМХ'
for a1 in letters:
    for a2 in letters:
        for a3 in letters:
            for a4 in letters:
                for a5 in letters:
                    for a6 in letters:
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('Р') + word.count('З') + word.count('М') + word.count('Х') >= 3:
                            count += 1
print('#6:', count)

'---------------------------------'

k = 10
N = 26
i = 5
Ip = int(k * i / 8) + 1
I = Ip + 15
n = int(4 * 2**10 / I)
print('#8:', n)

'---------------------------------'

maxim = 0
for x in range(100):
    for y in range(100):
        a = (3 + 2 * 4**x) * 4**x + 3 + 4**y
        summ = 0
        while a:
            summ += a % 4
            a //= 4
        maxim = max(maxim, summ)
print('#10:', maxim)

'---------------------------------'

a = 128**30 + 16**60 - 16
count = 0
while a:
    if a % 8 == 7:
        count += 1
    a //= 8
print('#12:', count)

'---------------------------------'

for a in range(10000, 0, -1):
    for x in range(1, 10000):
        if not(70 % a == 0 and (x % a == 0 or (x % 18 != 0 or x % 42 != 0))):
            break
    else:
        print('#15:', a)
        break


'''
    #2: 48
    #4: 1
    #6: 15360
    #8: 186
    #10: 9
    #12: 68
    #15: 14
'''

def is_simple(a):
    for dev in range(2, int(a**0.5) + 1):
        if i % dev == 0:
            return False
    return True


def summa(a):
    ans = 0
    while a != 0:
        ans += a % 10
        a //= 10
    return ans


print('\nNumber 1')
for i in range(126849, 126871 + 1):
    divs = [1, i]
    for div in range(2, int(i ** 0.5) + 1):
        if i % div == 0:
            divs.append(div)
            divs.append(i // div)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        divs.sort()
        print(*divs)

print('---------------------')

print('Number 2')
for i in range(1820348, 2880927 + 1):
    divs = [1, i]
    if i ** 0.5 % 1 == 0:
        divs.append(int(i ** 0.5))
    else:
        continue
    for div in range(2, int(i ** 0.5)):
        if i % div == 0:
            divs.append(div)
            divs.append(i // div)
            if len(divs) > 5:
                break
    if len(divs) == 5:
        divs.sort()
        print(*divs)

print('-------------------')
print('Number 3')
count = 0
for i in range(2943444, 2943529 + 1):
    if is_simple(i):
        count += 1
        print(count, i)

print('-------------------')
print('Number 4')
for i in range(33333, 55555 + 1):
    if is_simple(i) and summa(i) > 35:
        print(i, summa(i))

'''
Number 1
1 3 42283 126849
1 47 2699 126853
1 5 25373 126865
1 293 433 126869
---------------------
Number 2
1 37 1369 50653 1874161
1 41 1681 68921 2825761
-------------------
Number 3
1 2943467
2 2943491
3 2943503
4 2943527
-------------------
Number 4
39799 37
39979 37
39989 38
48799 37
48889 37
48989 38
49789 37
49999 40
'''

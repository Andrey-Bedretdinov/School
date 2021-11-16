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
    count += 1
    if is_simple(i):
        print(count, i)

print('-------------------')
print('Number 4')
numbers = []
for i in range(33333, 55555 + 1):
    if is_simple(i) and summa(i) > 35:
        numbers.append(i)
print(*numbers)

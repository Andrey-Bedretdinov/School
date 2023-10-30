def is_simple(a):
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    return True


# Number 1
print('\nNumber 1:')
for i in range(106732567, 152673836 + 1):
    if i ** 0.5 % 1 != 0:
        continue
    divs = set()
    for div in range(2, int(i ** 0.5) + 1):
        if i % div == 0:
            div1 = div
            div2 = i // div
            divs.add(div1)
            divs.add(div2)
        if len(divs) > 3:
            continue
    if len(divs) == 3:
        print(i, max(divs))

'---------------------------------------------'

# Number 2
print('\nNumber 2:')
for i in range(11275, 16328 + 1):
    divs = set()
    for div in range(1, int(i ** 0.5) + 1):
        if i % div == 0:
            div1 = div
            div2 = i // div
            divs.add(div1)
            divs.add(div2)
    if len(divs) == 5:
        divs = list(divs)
        divs.sort()
        print(*divs)

'---------------------------------------------'

# Number 3
print('\nNumber 3:')
count = 1
for i in range(1547341, 1547409):
    if is_simple(i):
        print(count, i)
        count += 1

'---------------------------------------------'


# Number 5
def f(start, end):
    if end < start or start == 12:
        return 0
    if end == start:
        return 1
    return f(start + 1, end) + f(start + 3, end)


print('\nNumber 5:')
print(f(7, 27) * f(27, 50))


'''
    Number 1:
    112550881 1092727
    131079601 1225043
    141158161 1295029
    
    Number 2:
    1 11 121 1331 14641
    
    Number 3:
    1 1547347
    2 1547383
    3 1547389
    4 1547407
    
    Number 5:
    2100006
'''
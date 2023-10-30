def is_simple(a):
    for div in range(2, int(a**0.5) + 1):
        if a % div == 0:
            return False
    return True


# Number 1
print('\nNumber 1:')
for i in range(190201, 190280 + 1):
    divs = set()
    for div in range(1, int(i**0.5) + 1):
        if i % div == 0:
            div1 = div
            div2 = i // div
            if div1 % 2 == 0:
                divs.add(div1)
            if div2 % 2 == 0:
                divs.add(div2)
    if len(divs) == 4:
        divs = list(divs)
        divs.sort(reverse=True)
        print(*divs)

'-------------------------------------------'

# Number 2
print('\nNumber 2:')
count = 1
for i in range(4671032, 4671106 + 1):
    if is_simple(i):
        print(count, i)
        count += 1

'-------------------------------------------'

# Number 3
print('\nNumber 3:')
for i in range(321654, 654321 + 1):
    divs = set()
    for div in range(2, int(i**0.5) + 1):
        if i % div == 0:
            div1 = div
            div2 = i // div
            if div1 % 2 == 0 or div2 % 2 == 0:
                break
            divs.add(div1)
            divs.add(div2)
    else:
        if len(divs) > 70:
            print(i, max(divs))


'''
    Number 1:
    190226 838 454 2
    190234 17294 22 2
    190238 2606 146 2
    190252 95126 4 2
    190258 758 502 2
    190274 27182 14 2
    190276 95138 4 2
    
    Number 2:
    1 4671071
    2 4671077
    3 4671097
    4 4671101
    
    Number 3:
    405405 135135
    530145 176715
    592515 197505
    626535 208845
'''


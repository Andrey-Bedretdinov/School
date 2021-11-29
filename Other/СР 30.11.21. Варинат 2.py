def is_simple(a):
    for i in range(2, int(a**0.5 + 1)):
        if a % i == 0:
            return False
    return True


# Number 1
print('\nNumber 1:')
for i in range(190061, 190080 + 1):
    divs = set()
    for div in range(1, int(i**0.5) + 1):
        if i % div == 0:
            div1 = div
            div2 = i // div
            if div1 % 2 == 1:
                divs.add(div1)
            if div2 % 2 == 1:
                divs.add(div2)
    if len(divs) == 4:
        divs = list(divs)
        divs.sort(reverse=True)
        print(*divs)

'---------------------------------------------'

# Number 2
print('\nNumber 2:')
count = 1
for i in range(4202865, 4202923 + 1):
    if is_simple(i):
        print(count, i)
        count += 1

'---------------------------------------------'

# Number 3
print('\nNumber 3:')
for i in range(25317, 51237 + 1):
    divs = set()
    for div in range(2, int(i**0.5) + 1):
        if i % div == 0:
            div1 = div
            div2 = i // div
            if is_simple(div1):
                divs.add(div1)
            if is_simple(div2):
                divs.add(div2)
    if len(divs) >= 6:
        print(i, max(divs))


'''
    Number 1:
    190061 6131 31 1
    11879 1697 7 1
    190067 2677 71 1
    23759 1033 23 1
    190073 14621 13 1
    95039 13577 7 1
    190079 2837 67 1
    
    Number 2:
    1 4202897
    2 4202899
    3 4202903
    4 4202911
    5 4202923
    
    Number 3:
    30030 13
    39270 17
    43890 19
    46410 17
'''
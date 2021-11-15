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

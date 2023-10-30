# Number 2
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if ((z and y) or ((x <= z) == (y <= w))) == 0 and x == 1:
                    print(x, y, z, w)

# Number 6
chars = 'АНДРЕЙ'
count = 0
for a1 in chars:
    for a2 in chars:
        for a3 in chars:
            for a4 in chars:
                for a5 in chars:
                    for a6 in chars:
                        for a7 in chars:
                            word = a1+a2+a3+a4+a5+a6+a7
                            if word[0] != 'Й' and word.count('А') == 1 and word.count('Й') == 1:
                                count += 1
print(count)

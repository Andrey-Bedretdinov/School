print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if ((x == (not y)) <= (z == (y or w))) == 0 and z != 1:
                    print(x, y, z, w)


a = 4**14 + 2**32 - 4
a = bin(a)[2:]
print(a.count('1'))

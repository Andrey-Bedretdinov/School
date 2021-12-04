# Ходы (+2, *2), Начало (5, S), Выигрыш >=69
def f(x, y, p):
    if x + y >= 69 and p == 3:
        return True
    else:
        if x + y < 69 and p == 3:
            return False
    return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 2, p + 1)


for i in range(1, 10000):
    if f(5, i, 1):
        print('\nNumber 1:', i)
        break


'-------------------------------------------------------------------------------------------------'


# Ходы (+2, *2), Начало (5, S), Выигрыш >=69
def f(x, y, p):
    if x + y >= 69 and p == 4:
        return True
    else:
        if (x + y < 69 and p == 4) or x + y >= 69:
            return False
    if p % 2 == 1:
        return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 2, p + 1)


ans = []
for i in range(1, 100):
    if f(5, i, 1):
        ans.append(i)
print('Number 2:', min(ans))


'-------------------------------------------------------------------------------------------------'


# Ходы (+2, *2), Начало (5, S), Выигрыш >=69
def f(x, y, p):
    if x + y >= 69 and (p == 3 or p == 5):
        return True
    else:
        if (x + y < 69 and p == 5) or x + y >= 69:
            return False
    if p % 2 == 0:
        return f(x + 2, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 2, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 2, p + 1)


def f1(x, y, p):
    if x + y >= 69 and (p == 3 or p == 5):
        return True
    else:
        if (x + y < 69 and p == 3) or x + y >= 69:
            return False
    if p % 2 == 0:
        return f1(x + 2, y, p + 1) or f1(x * 2, y, p + 1) or f1(x, y + 2, p + 1) or f1(x, y * 2, p + 1)
    else:
        return f1(x + 2, y, p + 1) and f1(x * 2, y, p + 1) and f1(x, y + 2, p + 1) and f1(x, y * 2, p + 1)


ans1 = []
for i in range(1, 100):
    if f(5, i, 1):
        ans1.append(i)
ans2 = []
for i in range(1, 100):
    if f1(5, i, 1):
        ans2.append(i)
print('Number 3:', *(set(ans1) - set(ans2)))


'''
    Number 1: 16
    Number 2: 29
    Number 3: 27 28
'''
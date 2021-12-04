# Ходы (+1, *2), Начало (9, S), Выигрыш >=40
def f(x, y, p):
    if x + y >= 40 and p == 3:
        return True
    else:
        if x + y < 40 and p == 3:
            return False
    return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)


for i in range(1, 100):
    if f(9, i, 1):
        print('\nNumber 1:', i)
        break


'-----------------------------------------------------------------------------------------------'


# Ходы (+1, *2), Начало (9, S), Выигрыш >=40
def f(x, y, p):
    if x + y >= 40 and p == 4:
        return True
    else:
        if (x + y < 40 and p == 4) or x + y >= 40:
            return False
    if p % 2 == 1:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)


ans = []
for i in range(1, 100):
    if f(9, i, 1):
        ans.append(i)
print('Number 2:', *ans)


'-----------------------------------------------------------------------------------------------'


# Ходы (+1, *2), Начало (9, S), Выигрыш >=40
def f(x, y, p):
    if x + y >= 40 and (p == 3 or p == 5):
        return True
    else:
        if (x + y < 40 and p == 5) or x + y >= 40:
            return False
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)


def f1(x, y, p):
    if x + y >= 40 and (p == 3 or p == 5):
        return True
    else:
        if (x + y < 40 and p == 3) or x + y >= 40:
            return False
    if p % 2 == 0:
        return f1(x + 1, y, p + 1) or f1(x * 2, y, p + 1) or f1(x, y + 1, p + 1) or f1(x, y * 2, p + 1)
    else:
        return f1(x + 1, y, p + 1) and f1(x * 2, y, p + 1) and f1(x, y + 1, p + 1) and f1(x, y * 2, p + 1)


ans1 = []
for i in range(1, 100):
    if f(9, i, 1):
        ans1.append(i)
ans2 = []
for i in range(1, 100):
    if f1(9, i, 1):
        ans2.append(i)
print('Number 3:', *(set(ans1) - set(ans2)))


'''
    Number 1: 4
    Number 2: 3 14
    Number 3: 0
'''
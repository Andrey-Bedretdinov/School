def f7(x_):
    r_ = []
    x_ = str(x_)
    for i_ in x_:
        r_.append(int(i_))
    if 0 in r_:
        return False
    x_ = int(x_)
    for div in r_:
        if x_ % div == 0:
            continue
        return False
    return True


a = int(input('Введите натуральное число: '))
numbers = []
for i in range(a + 1):
    if f7(i):
        numbers.append(i)
print(numbers)

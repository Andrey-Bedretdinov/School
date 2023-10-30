def f(n):
    s = '1' * n
    while ('111' in s) or ('222' in s):
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
        print(s)
    for i in s:
        if i != '1':
            return False
    print(s)
    return True


for i in range(201, 1000000):
    if f(i):
        print(i)
        break
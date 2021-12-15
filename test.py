def f(a):
    a = bin(a)[2:]
    if a.count('1') > a.count('0'):
        a += '0'
    else:
        a = '11' + a
    return int(a, 2)


for i in range(1, 1000000):
    if f(f(i)) > 500:
        print(i)
        break

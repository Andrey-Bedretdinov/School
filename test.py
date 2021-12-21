def f(s):
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    return s.count('1')


minim = 1111111111111111
count = 0
for i in range(201, 10000):
    if f('1' * i) > count:
        count = f('1' * i)
        minim = min(minim, i)
print(minim, count)

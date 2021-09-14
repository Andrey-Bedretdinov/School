a = int(input())
f0 = 0
f1 = 1
i = 1
while i != a:
    x = f1 + f0
    f0 = f1
    f1 = x
    i += 1
if a == 0:
    print(0)
elif a == 1:
    print(1)
else:
    print(x)

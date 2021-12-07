a = int(input())
i = 0
n = 0
while a != 0:
    if a > i:
        i = a
        n = 0
    if a == i:
        n += 1
    a = int(input())
print(n)

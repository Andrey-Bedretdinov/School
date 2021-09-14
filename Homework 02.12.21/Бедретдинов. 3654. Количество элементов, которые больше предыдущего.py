a = int(input())
i = 0
y = a
while a != 0:
    if a > y:
        i += 1
    y = a
    a = int(input())
print(i)

a = int(input())
i = 10 ** a - 1
while i >= 10 ** (a - 1):
    print(i)
    i -= 2

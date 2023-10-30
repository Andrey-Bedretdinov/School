x, p, y = int(input()), int(input()), int(input())
i = 0
while x < y:
    x += x * p / 100
    rub = x // 1
    cop = x % 1 // 0.01 / 100
    x = rub + cop
    i += 1
print(i)

def IsPointInSquare(x, y):
    return y <= x + 1 and y <= -x + 1 and y >= -x - 1 and y >= x - 1


if IsPointInSquare(float(input()), float(input())):
    print('YES')
else:
    print('NO')

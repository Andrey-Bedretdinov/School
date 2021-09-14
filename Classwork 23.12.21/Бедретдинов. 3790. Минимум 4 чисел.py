def min2(a, b):
    return min(a, b)


def min4(a, b, c, d):
    return min2(min2(a, b), min2(c, d))


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))

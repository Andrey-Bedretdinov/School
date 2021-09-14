a, b, c = int(input()), int(input()), int(input())
if a + b <= c or a + c <= b or b + c <= a:
    print('impossible')
elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
    print('rectangular')
elif a ** 2 > b ** 2 + c ** 2 or b ** 2 > a ** 2 + c ** 2 or c ** 2 > a ** 2 + b ** 2:
    print('obtuse')
else:
    print('acute')

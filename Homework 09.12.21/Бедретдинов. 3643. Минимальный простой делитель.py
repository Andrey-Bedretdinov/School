number = int(input())
if number % 2 == 0:
    print(2)
else:
    divider = 3
    while number % divider != 0 and divider ** 2 <= number:
        divider += 2
    if number % divider == 0:
        print(divider)
    else:
        print(number)

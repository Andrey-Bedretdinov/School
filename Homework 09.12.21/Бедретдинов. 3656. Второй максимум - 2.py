number = int(input())
max1 = 0
max2 = 0
while number != 0:
    if number >= max1:
        max2 = max1
        max1 = number
    elif max2 < number < max1:
        max2 = number
    number = int(input())
print(max2)

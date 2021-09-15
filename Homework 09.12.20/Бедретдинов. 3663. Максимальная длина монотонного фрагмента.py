number = int(input())
k = 0
# Если k=0, то последовательность убывает
# Если k=1, то последовательность возрастает
# Следовательно, при изменении k, начинается новый монотонный промежуток
count = 1
max_length = 0
last_number = number
number = int(input())
while number != 0:
    if number > last_number and k == 1:
        count += 1
    elif number > last_number and k == 0:
        if count > max_length:
            max_length = count
        count = 2
        k = 1
    elif number < last_number and k == 0:
        count += 1
    elif number < last_number and k == 1:
        if count > max_length:
            max_length = count
        count = 2
        k = 0
    else:
        if count > max_length:
            max_length = count
        count = 1
    last_number = number
    number = int(input())
if count > max_length:
    max_length = count
print(max_length)

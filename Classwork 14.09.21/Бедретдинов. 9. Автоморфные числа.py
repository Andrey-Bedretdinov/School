n = int(input('Введите натуральное число: '))
numbers = []
for i in range(n + 1):
    i_ = str(i**2)
    if i_[-len(str(i)):] == str(i):
        numbers.append(i)
print(numbers)

f = open('17.txt', 'r')
numbers = []
for line in f:
    numbers.append(int(line[:-1]))
k = 0
maxim = 0
for i in range(1, len(numbers)):
    if (numbers[i - 1] % 3 == 0 or numbers[i] % 3 == 0) and (numbers[i - 1] + numbers[i]) % 5 == 0:
        k += 1
        if numbers[i - 1] + numbers[i] > maxim:
            maxim = numbers[i - 1] + numbers[i]
print(k, maxim)
from itertools import combinations

# 17
with open('17-3.txt', 'r') as file:
    data = []
    for line in file:
        data.append(int(line))

count = 0
max_sum = 0
for i in range(len(data) - 2):
    numbers = [data[i], data[i + 1], data[i + 2]]
    numbers.sort(reverse=True)
    if numbers[0] ** 2 < numbers[1] ** 2 + numbers[2] ** 2:
        count += 1
        max_sum = max(max_sum, sum(numbers))

print(count, max_sum)

# 24
with open('inf_26_04_21_24.txt', 'r') as file:
    data = []
    for line in file:
        data.append(line)

for line in data:
    if line.count('G') >= 25:
        data.remove(line)

max_d = 0
for line in data:
    for char in line:
        if line.count(char) >= 2:
            first = line.find(char)
            last = line.rfind(char)
            max_d = max(max_d, last - first)

print(max_d)

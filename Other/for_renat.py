import itertools

with open('17.txt', 'r') as file:
    data = file.read().split('\n')
    data = list(int(x) for x in data)

count = 0
max_sum = 0
i = 0
combinations = itertools.combinations(data, 2)

for i in combinations:
    a, b = i
    if a * b % 62 == 0:
        count += 1
        max_sum = max(max_sum, a + b)

print(count, max_sum)

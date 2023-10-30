with open('24.txt') as file:
    data = file.read()

count = 0
maxim = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        count += 1
    else:
        maxim = max(maxim, count)
        count = 1
print(maxim)


with open('24-1.txt') as file:
    data = file.read()

maxim = 0
indexes = []
for i in range(1, len(data) - 1):
    if data[i - 1] <= data[i] and data[i + 1] <= data[i]:
        indexes.append(i)

for i in range(len(indexes) - 1):
    maxim = max(maxim, indexes[i + 1] - indexes[i])
print(maxim)

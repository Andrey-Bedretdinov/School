# Number 2
count = 0
data = []
for i in open('17-4.txt'):
    data.append(int(i))
numbers = []
for i in data:
    if (i % 3) == (i % 5) and (i % 31 == 0 or i % 47 == 0 or i % 53 == 0):
        numbers.append(i)
print('#2:', len(numbers), min(numbers))

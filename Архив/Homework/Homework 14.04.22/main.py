# Number 2
from pprint import pprint

with open('24-2.txt') as file:
    data = file.read()

chars = {}
for i in range(65, 91):
    chars[chr(i)] = 0

for i in range(1, len(data) - 1):
    if data[i - 1] == data[i + 1]:
        chars[data[i]] += 1

maxim = 0
char = ''
for i in chars:
    if chars[i] > maxim:
        char = i
        maxim = chars[i]
print('Number #2:', char)

# Number 3
with open('27-A_1.txt') as file:
    data = []
    for line in file:
        elem = line.strip('\n').split(' ')
        elem.remove('')
        para = []
        [para.append(int(x)) for x in elem]
        data.append(para)

print(data)


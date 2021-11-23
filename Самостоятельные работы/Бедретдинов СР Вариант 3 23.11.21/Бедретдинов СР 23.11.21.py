# Number 1
file = open('k7-42.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for char in data:
    if char == 'C':
        count += 1
        continue
    elif max_count < count:
        max_count = count
    count = 0
print('Number 1:', max_count)

'------------------------------------------------------------------------------------------------------'

# Number 2
file = open('k7a-6.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for char in data:
    if char in 'BCDF':
        count += 1
        continue
    elif max_count < count:
        max_count = count
    count = 0
print('Number 2:', max_count)

'------------------------------------------------------------------------------------------------------'

# Number 3
file = open('k7b-4.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for char in data:
    if (char == 'E' and count % 4 == 0) or \
            (char == 'B' and count % 4 == 1) or \
            (char == 'C' and count % 4 == 2) or \
            (char == 'F' and count % 4 == 3):
        count += 1
        continue
    elif max_count < count:
        max_count = count
    count = 0
    if char == 'E':
        count = 1
print('Number 3:', max_count)

'------------------------------------------------------------------------------------------------------'

# Number 4
file = open('k8-20.txt')
data = file.read()
file.close()
count = 1
max_count = 0
max_char = ''
for i in range(1, len(data)):
    if data[i - 1] == data[i]:
        count += 1
        continue
    elif max_count < count:
        max_count = count
        max_char = data[i - 1]
    count = 1
print('Number 4:', max_char, max_count)

'------------------------------------------------------------------------------------------------------'

# Number 5
file = open('24.txt')
data = file.read()
file.close()
count = 1
max_count = 0
index_last_char = 0
for i in range(1, len(data)):
    if ord(data[i]) < ord(data[i - 1]):
        count += 1
        continue
    elif max_count < count:
        max_count = count
        index_last_char = i - 1
    count = 1
number_max_char = index_last_char - max_count + 1
print('Number 5:', number_max_char)


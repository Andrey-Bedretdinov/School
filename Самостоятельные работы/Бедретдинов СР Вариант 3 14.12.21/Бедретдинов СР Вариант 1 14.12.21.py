# Number 1
data = []
maxim = 0
count = 0
for i in open('17-3.txt'):
    data.append(int(i))
for i in range(len(data) - 2):
    if (data[i] * data[i + 1] * data[i + 2]) % 7 == 0 and (data[i] + data[i + 1] + data[i + 2]) % 10 == 5:
        count += 1
        maxim = max(maxim, data[i] + data[i + 1] + data[i + 2])
print('#1:', count, maxim)

'-----------------------'

# Number 2
data = []
minim = 111111111111111
count = 0
for i in open('17-4.txt'):
    data.append(int(i))
for i in data:
    if i % 3 == i % 5 and (i % 31 == 0 or i % 47 == 0 or i % 53 == 0):
        count += 1
        minim = min(minim, i)
print('#2:', count, minim)

'-----------------------'

# Number 3
data = []
maxim = 0
count = 0
for i in open('17-4.txt'):
    data.append(int(i))
for i in data:
    if i % 5 == 3 and i % 9 == 5 and i % 8 != 7:
        count += 1
        maxim = max(maxim, i)
print('#3:', count, maxim)


'''
    #1: 153 19285
    #2: 31 1081
    #3: 43 9653
'''

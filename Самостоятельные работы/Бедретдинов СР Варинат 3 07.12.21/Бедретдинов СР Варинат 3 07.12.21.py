# Number 1
count = 0
raz = 100000000
data = []
for i in open('17-3.txt'):
    data.append(int(i))
for i in range(len(data) - 2):
    troyka = [data[i], data[i + 1], data[i + 2]]
    if troyka[0] <= troyka[1] <= troyka[2]:
        raz = min(raz, max(troyka) - min(troyka))
        count += 1
print('\n#1:', count, raz)

'-----------------------------------------------'

# Number 2
count = 0
data = []
for i in open('17-4.txt'):
    data.append(int(i))
numbers = []
for i in data:
    if i % 3 == 0 and i % 9 != 0 and i % 10 >= 4:
        numbers.append(i)
print('#2:', len(numbers), sum(numbers) // len(numbers))

'-----------------------------------------------'

# Number 3
count = 0
data = []
for i in open('17-4.txt'):
    data.append(int(i))
numbers = []
for i in data:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        numbers.append(i)
print('#3:', max(numbers) - min(numbers), len(numbers))


'''
    #1: 832 460
    #2: 247 5706
    #3: 8515 126
'''

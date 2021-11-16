file = open('24-157.txt', 'r')
data = file.read()
file.close()
chars = {}
for i in range(65, 91):
    chars[chr(i)] = 0
print(chars)

for i in range(1, len(data) - 1):
    if data[i - 1] == data[i + 1]:
        chars[data[i]] += 1


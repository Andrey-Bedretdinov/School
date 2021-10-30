f = open('24.txt', 'r')
line = f.read()
k = 0
count = 0
maxim = 0
for i in line:
    if i == 'A' and k < 1:
        k += 1
    elif i == 'A' and k >= 1:
        if count > maxim:
            maxim = count
        count = 1
        k = 1
        continue
    count += 1
print(maxim)


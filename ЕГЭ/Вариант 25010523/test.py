# Number 26
with open('26 (1).txt') as file:
    data = []
    for line in file:
        data.append([int(x) for x in line.strip('\n').split(' ')])

xy = {}

c = 0
for i in data:
    if not xy.get(i[0]):
        xy[i[0]] = []

    xy[i[0]].append(i[1])
    xy[i[0]].sort()

    c += 1
    if c % 1000 == 0:
        print(c)


maxim = 0
mx = 0
u = 0

for x in xy:
    for y in range(len(xy[x]) - 1):
        a, b = xy[x][y], xy[x][y + 1]
        if b - a - 1 >= maxim:
            maxim = b - a - 1
            mx = x

print(xy)
print(mx, maxim)




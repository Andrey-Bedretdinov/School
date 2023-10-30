# Number 26
with open('26.txt') as file:
    n = int(file.readline())
    data = []
    for line in file:
        data.append([int(x) for x in line.strip('\n').split(' ')])

xy = {}
for i in data:
    if not xy.get(i[0]):
        xy[i[0]] = []
    xy[i[0]].append(i[1])
    xy[i[0]].sort()

maxi = 0
max_x = 0
for x in xy:
    count = 0
    if len(xy[x]) > 1:
        for y in range(len(xy[x]) - 1):
            a, b = xy[x][y], xy[x][y + 1]
            if b - a == 1:
                if count == 0:
                    count += 2
                else:
                    count += 1
                    if count >= maxi:
                        maxi = count
                        max_x = max(max_x, x)
            else:
                count = 0

print(max_x, maxi)  # 24 14
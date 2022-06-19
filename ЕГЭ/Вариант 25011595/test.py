# Number 26
with open('26.txt') as file:
    n = int(file.readline())
    data = []
    for _ in range(n):
        line = [int(x) for x in file.readline().strip('\n').split(' ')]
        data.append(line)

xy = {}
for i in data:
    if not xy.get(i[0]):
        xy[i[0]] = []
    xy[i[0]].append(i[1])
    xy[i[0]].sort()


maxi_x = 0
mini_y = 10**20
for x in xy:
    if len(xy[x]) < 2:
        continue

    for i in range(len(xy[x]) - 1):
        a, b = xy[x][i], xy[x][i + 1]
        if b - a - 1 == 13:  # Поменять на 13!!!
            maxi_x = x
            mini_y = a + 1
            break

print(maxi_x, mini_y)  # 56588 67073


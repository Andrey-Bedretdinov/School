from itertools import combinations


def bin_search(x, data):
    l, r = 0, len(data)
    while l < r - 1:
        c = (l + r) // 2
        if x < data[c]:
            r = c
        else:
            l = c
    if data[l] == x:
        return True
    return False


with open('36881.txt', 'r') as file:
    data = []
    for line in file:
        data.append(int(line))
data.sort()
combinations = combinations(data, 2)
count = 0
max_sum = 0
for i in combinations:
    if i[0] % 2 == i[1] % 2 and bin_search(i[0] + i[1], data):
        count += 1
        max_sum = max(max_sum, i[0] + i[1])
print(count, max_sum)

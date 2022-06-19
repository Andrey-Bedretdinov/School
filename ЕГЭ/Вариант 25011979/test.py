# Number 26
with open('26 (1).txt') as file:
    k, n = [int(x) for x in file.readline().split(' ')]
    mesta = [int(file.readline()) for _ in range(k)]
    stud = []
    for _ in range(n):
        line = [int(x) for x in file.readline().split(' ')]
        stud.append(line)

kolvo = {}
for i in range(k):
    kolvo[i] = 0

for i in stud:
    kolvo[i[1]] += 1

concurs = []
for i in range(k):
    concurs.append(kolvo[i] / mesta[i])

count = 0
for i in range(k):
    if concurs[i] >= 1:
        count += mesta[i]
    else:
        count += kolvo[i]
print(count)  # 55255

print(mesta[15], kolvo[15])

c15 = []
for i in stud:
    if i[1] == 15:
        c15.append(i[0])
c15.sort(reverse=True)
print(c15[24])  # 266







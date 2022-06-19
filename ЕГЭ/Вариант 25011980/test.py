# Number 27
from itertools import combinations


def get_divs(j):
    divs = set()
    for div in range(1, int(j**0.5) + 1):
        if j % div == 0:
            divs.add(div)
            divs.add(j // div)
    return divs


def get_nod(p):
    p = list(p)
    ls = []
    [ls.append(get_divs(x)) for x in p]
    while len(ls) != 1:
        a, b = ls[0], ls[1]
        ls.remove(a)
        ls.remove(b)
        ls.append(a & b)
    try:
        return max(list(ls[0]))
    except:
        return 0


with open('27-B.txt') as file:
    n, k = [int(x) for x in file.readline().strip('\n').split(' ')]
    data = [int(file.readline()) for _ in range(n)]

c = list(combinations(data, 3))
maxi = 0
for i in c:
    maxi = max(maxi, get_nod(i))
print(maxi)



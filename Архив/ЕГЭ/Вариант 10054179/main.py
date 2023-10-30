'''
# Number 2
print('x y z F')  # (¬z)∧x
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            a = not z and x
            if not a:
                a = 0
            print(x, y, z, a)


# Number 4
'Д - 000, Х - 001, Р - 010, О - 011, В - 100'

# Number 5
def f(n):
    n_ = n
    n = bin(n)[2:]
    n = n.replace('1', '0', 1)
    n = int(n, 2)
    return n_ - n

ans = set()
for i in range(10, 1001):
    ans.add(f(i))
print(len(ans))


# Number 6
s = 0
n = 170
while s + n < 325:
    s = s + 25
    n = n - 5
print(s)


# Number 8
from itertools import permutations
permutations = list(permutations('МАТВЕЙ'))
count = 0
for i in permutations:
    word = i[0] + i[1] + i[2] + i[3] + i[4]
    if word[0] != 'Й' and not 'АЕ' in word:
        count += 1
print(count)


# Number 14
def f(n, i):
    ans = ''
    while n != 0:
        ans = str(n % i) + ans
        n //= i
    return ans

for x in range(10000):
    if len(str(f(x, 6))) == 2 and len(str(f(x, 5))) == 3 and str(f(x, 11))[-1] == '1':
        print(x)


# Number 16
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + n
print(f(40))


# Number 17
with open('17-3.txt', 'r') as file:
    data = []
    for line in file:
        data.append(int(line))

not_even = []
for i in data:
    if i % 2 == 1:
        not_even.append(i)
arif = sum(not_even) / len(not_even)

count = 0
max_sum = 0
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if (a % 5 == 0 or b % 5 == 0) and (a < arif or b < arif):
        count += 1
        max_sum = max(max_sum, a + b)

print(count, max_sum)


# Number 19
from functools import lru_cache
import sys
sys.setrecursionlimit(2000)

def moves(p):
    a, b = p
    if a % 2 == 1:
        ost1 = a // 2 + 1
    else:
        ost1 = a // 2
    if b % 2 == 1:
        ost2 = b // 2 + 1
    else:
        ost2 = b // 2
    if a == 1:
        return (a, ost2), (a - 1, b), (a, b - 1)
    if b == 1:
        return (ost1, b), (a - 1, b), (a, b - 1)
    return (ost1, b), (a, ost2), (a - 1, b), (a, b - 1)


@lru_cache(None)
def f(p):

    if sum(p) <= 40:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'


for s in range(21, 78):
    print(s, f((20, s)))


# Number 22
def f(x):
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 6
        x = x // 6
    return a, b

for i in range(1, 100000):
    if f(i) == (2, 4):
        print(i)
        break


# Number 23
def f(start, stop):
    if start > stop or start == 15:
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start + 2, stop)

print(f(3, 9) * f(9, 20))


with open('24-2.txt', 'r') as file:
    data = []
    for line in file:
        data.append(line)

min_len = 1000000
string = ''
for line in data:
    if len(line) < min_len:
        min_len = len(line)
        string = line

max_count = 0
letter_ = ''
string = sorted(string)
for letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    if max_count < string.count(letter):
        max_count = string.count(letter)
        letter_ = letter
print(letter_)


# Number 25
def get_m(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return i + a // i
    return 0

k = 0
for i in range(452022, 100000000):
    if k >= 5:
        break
    if get_m(i) % 7 == 3:
        print(i, get_m(i))
        k += 1


# Number 26
with open('26.txt', 'r') as f:
    data = []
    for line in f:
        data.append(int(line))
data.sort()

last = 0
count = 0
massa = 0
while massa <= 99990:
    cont = data[0]
    data.remove(cont)
    massa += cont
    count += 1
    last = cont
print(count - 1, last)
'''

# Number 27
with open('27-B.txt', 'r') as file:
    data = []
    for line in file:
        data.append(int(line))

ld = len(data)
combinations = []
for i1 in range(ld - 2):
    print(i1)
    for i2 in range(i1 + 1, ld - 1):
        for i3 in range(i2 + 1, ld):
            combinations.append([data[i1] + data[i2] + data[i3]])

min_sum = 1000000000
for i in combinations:
    if sum(i) % 3 == 0:
        min_sum = min(min_sum, sum(i))
print(min_sum)
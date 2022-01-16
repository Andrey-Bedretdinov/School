'''import posix

with open('test.txt', 'r') as file:
    data = file.read().replace('\n', ' ').replace('(', ' ').split(' ')
    defs = []
    for i in range(len(data)):
        if data[i] == 'def':
            defs.append(data[i + 1])

defs = list(x.replace('_', ' ').title().replace(' ', '') + 'Error' for x in defs)
print(defs)
string = 'class f(Exception):\n    pass'
result = []
for i in defs:
    result.append(string.replace('f', i))

for i in result:
    print(i + '\n')
'''
from time import sleep


class ans(Exception):
    pass


try:
    s = 1 / 0
except Exception:
    print(ans)
sleep(5)
print(1)

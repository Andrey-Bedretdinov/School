import posix

with open('test.txt', 'r') as file:
    data = file.read().replace('\n', ' ').replace('(', ' ').split(' ')
    defs = []
    for i in range(len(data)):
        if data[i] == 'def':
            defs.append(data[i + 1])

defs = list(x.replace('_', ' ').title().replace(' ', '') + 'Error' for x in defs)
print(*defs)


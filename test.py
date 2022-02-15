from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 59:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'
    if any(f(x) == 'П2' or f(x) == 'П1' for x in moves(p)):
        return 'В3'


for i in range(1, 55):
    if f((5, i)) == 'П1':
        print(i)
        break

for i in range(1, 55):
    if f((5, i)) == 'В2':
        print(i)
        break

print('---')
for i in range(1, 55):
    if f((5, i)) == 'П2':
        print(i)
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 3, b), (a * 2, b), (a, b + 3), (a, b * 2)


@lru_cache(None)
def f(p):
    if sum(p) >= 79:
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
    if all(f(x) == 'В2' or f(x) == 'В1' or f(x) == 'В3' for x in moves(p)):
        return 'П3'
    if any(f(x) == 'П2' or f(x) == 'П1' or f(x) == 'П3' for x in moves(p)):
        return 'В4'
    if all(f(x) == 'В2' or f(x) == 'В1' or f(x) == 'В3' or f(x) == 'В4' for x in moves(p)):
        return 'П4'


for i in range(1, 100):
    if f((9, i)) == 'В1':
        print(i)
        break

ans = []
for i in range(1, 100):
    if f((9, i)) == 'В2':
        ans.append(i)
print(len(ans))


ans = []
for i in range(1, 100):
    if f((9, i)) == 'П2':
        ans.append(i)
print(*ans, '\n')

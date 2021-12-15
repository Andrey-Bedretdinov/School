# 1420
from functools import lru_cache


def moves(p):
    a, b = p
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache()
def f(p):
    if p[0] * p[1] >= 63:
        return 'WIN'
    if any(f(x) == 'WIN' for x in moves(p)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(p)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(p)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(p)):
        return 'П2'


for i in range(1, 35):
    if f((2, i)) == 'П1':
        print('#19:', i)

ans = []
for i in range(1, 35):
    if f((2, i)) == 'В2':
        ans.append(i)
print('#20:', min(ans), max(ans))

ans = []
for i in range(1, 35):
    if f((2, i)) == 'П2':
        ans.append(i)
print('#20:', max(ans))

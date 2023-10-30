from functools import lru_cache


# Ходы (+1, +2, +3, *2), Начало 1<=s<=33, Конец >=34
def moves(h):
    return h + 1, h + 2, h + 3, h * 2


@lru_cache()
def f(s):
    if s >= 34:
        return 'END'
    if any(f(i) == 'END' for i in moves(s)):
        return 'В1'
    if all(f(i) == 'В1' for i in moves(s)):
        return 'П1'
    if any(f(i) == 'П1' for i in moves(s)):
        return 'В2'
    if all(f(i) == 'В2' or f(i) == 'В1' for i in moves(s)):
        return 'П2'


for i in range(1, 36):
    if f(i) == 'П1':
        print(i)
ans = []
for i in range(1, 36):
    if f(i) == 'В2':
        ans.append(i)
print(min(ans), max(ans))
ans = []
for i in range(1, 36):
    if f(i) == 'П2':
        ans.append(i)
print(*ans)


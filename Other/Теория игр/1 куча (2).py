from functools import lru_cache


def moves(a):
    return a + 1, a * 2, a * 3


# Ходы (+1, *2, *3), Выигрыш 72>=s>=43
@lru_cache()
def f(s):
    if s > 72:
        return 'В1'
    if 43 <= s:
        return 'END'
    if any(f(x) == 'END' for x in moves(s)):
        return 'В1'
    if all(f(x) == 'В1' for x in moves(s)):
        return 'П1'
    if any(f(x) == 'П1' for x in moves(s)):
        return 'В2'
    if all(f(x) == 'В2' or f(x) == 'В1' for x in moves(s)) or s > 72:
        return 'П2'


for i in range(1, 80):
    if f(i) == 'П1':
        print('\nNumber 19:', i)
        break
ans = []
for i in range(1, 80):
    if f(i) == 'В2':
        ans.append(i)
print('Number 20:', len(ans))
ans = []
for i in range(1, 80):
    if f(i) == 'П2':
        ans.append(i)
print('Number 21:', min(ans), max(ans))


'''
Number 19: 14
Number 20: 3
Number 21: 12 39
'''

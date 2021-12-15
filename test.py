from functools import lru_cache


def moves(p):
    return p + 1, p * 2, p * 3


@lru_cache()
def f(p):
    if p > 72:
        return 'В1'
    if p >= 43:
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


for i in range(1, 100):
    print(i, f(i))
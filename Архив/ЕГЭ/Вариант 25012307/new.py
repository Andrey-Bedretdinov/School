# Number 23
def f(start, stop):
    if start < stop:
        return 0
    if start == stop:
        return 1
    return f(start - 3, stop) + f(start // 2, stop)

print(f(108, 42) * f(42, 12))  # 30

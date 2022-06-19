# Number 23
def f(start, stop):
    if start > stop:
        return 0
    if start == stop:
        return 1
    return f(start + 2, stop) + f(start * 2, stop)


print(f(1, 18) * f(18, 52))  # 96




n, x, t = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

buffer = a

data = {}
for i in range(n):
    data[i + 1] = abs(a[i] - x)

sorted_values = sorted(data.values())
sorted_data = {}
for i in sorted_values:
    for k in data.keys():
        if data[k] == i:
            sorted_data[k] = data[k]
            break

ans = []
for key in sorted_data:
    if t - sorted_data[key] >= 0:
        ans.append(key)
        t -= sorted_data[key]
    else:
        break

print(len(ans))
print(*ans)

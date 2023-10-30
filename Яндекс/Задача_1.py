n = int(input())
ci = input().split(' ')
ri = input().split(' ')
k = int(input())
si = input().split(' ')

ans = 0
index_left = ci.index(si[0])
for i in range(1, k):
    index_right = ci.index(si[i])
    if ri[index_left] != ri[index_right]:
        ans += 1
    index_left = index_right

print(ans)

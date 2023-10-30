n = int(input())
last = 0
for number in range(1, n + 1):
    print(last * 10 + number)
    last = last * 10 + number

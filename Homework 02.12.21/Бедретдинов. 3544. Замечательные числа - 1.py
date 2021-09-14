i = 10
while i < 100:
    if i == ((i // 10) * (i % 10)) * 2:
        print(i)
    i += 1

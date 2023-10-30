string = input()
count = 0
for char in string:
    if 48 <= ord(char) <= 57:
        count += 1
print(count)

print('# Number 26')
numbers = []
for i in open('26 (25005908).txt'):
    numbers.append(int(i))
d1 = []
d2 = []
for i in range(10000):
    count = numbers.count(i)
    while count / 2 >= 1:
        d1.append(i)
        d2.append(i)
        numbers.remove(i)
        numbers.remove(i)
        count -= 2

print(len(numbers), end=' ')

while len(numbers):
    if sum(d1) > sum(d2):
        d2.append(max(numbers))
        numbers.remove(max(numbers))
        d2.append(max(numbers))
        numbers.remove(max(numbers))
        d1.append(min(numbers))
        numbers.remove(min(numbers))
        d1.append(min(numbers))
        numbers.remove(min(numbers))
    else:
        try:
            d1.append(max(numbers))
            numbers.remove(max(numbers))
            d1.append(max(numbers))
            numbers.remove(max(numbers))
            d2.append(min(numbers))
            numbers.remove(min(numbers))
            d2.append(min(numbers))
            numbers.remove(min(numbers))
        except Exception as ex:
            print(ex)
print(abs(sum(d1) - sum(d2)))

'''
1) В текстовом файле k7-3.txt находится цепочка из символов латинского алфавита A, B, C. Найдите
длину самой длинной подцепочки, состоящей из символов C.
'''

file = open('k7-3.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for char in data:
    if char == 'C':
        count += 1
        continue
    if max_count < count:
        max_count = count
    count = 0
print('1.', max_count)

'-------------------------------------------------------------------------------------------------------------------'

'''
2) В текстовом файле k7a-2.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, состоящей из символов A, C, D (в произвольном порядке).
'''

file = open('k7a-2.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for char in data:
    if char in 'ACD':
        count += 1
        continue
    if max_count < count:
        max_count = count
    count = 0
print('2.', max_count)

'-------------------------------------------------------------------------------------------------------------------'

'''
3) В текстовом файле k7b-2.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите максимальную длину цепочки вида DBACDBACDBAC.... (состоящей из фрагментов DBAC,
последний фрагмент может быть неполным).
'''

file = open('k7b-2.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for char in data:
    if (char == 'D' and count % 4 == 0) or \
            (char == 'B' and count % 4 == 1) or \
            (char == 'A' and count % 4 == 2) or \
            (char == 'C' and count % 4 == 3):
        count += 1
        continue
    if max_count < count:
        max_count = count
    count = 0
    if char == "D":
        count = 1
print('3.', max_count)

'-------------------------------------------------------------------------------------------------------------------'

'''
4) В текстовом файле k7c-2.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите количество цепочек длины 3, удовлетворяющих следующим условиям:
 1-й символ – один из A, C, E;
 2-й символ – один из A, D, F, который не совпадает с первым;
 3-й символ – один из A, B, F, который не совпадает со вторым.
'''

file = open('k7c-2.txt')
data = file.read()
file.close()
count = 0
for i in range(len(data) - 2):
    if data[i] in "ACE" and \
            data[i + 1] in "ADF" and data[i] != data[i + 1] and \
            data[i + 2] in "ABF" and data[i + 2] != data[i + 1]:
        count += 1
print('4.', count)

'-------------------------------------------------------------------------------------------------------------------'

'''
5) В текстовом файле k8-25.txt находится цепочка из символов, в которую могут входить заглавные
буквы латинского алфавита A…Z и десятичные цифры. Найдите длину самой длинной подцепочки,
состоящей из одинаковых символов. Если в файле несколько подходящих цепочек одинаковой длины,
нужно взять первую из них. Выведите сначала символ, из которого строится эта подцепочка, а затем через
пробел – длину этой подцепочки.
'''

file = open('k8-25.txt')
data = file.read()
file.close()
count = 1
max_count = 0
max_char = data[0]
last_char = data[0]
for char in data:
    if char == last_char:
        count += 1
        continue
    elif max_count < count:
        max_count = count
        max_char = last_char
    last_char = char
    count = 1
print('5.', max_char, max_count)

'-------------------------------------------------------------------------------------------------------------------'

'''
6) Текстовый файл k8-2.txt состоит не более чем из 10^6
символов. Определите максимальное количество
идущих подряд символов, среди которых каждые два соседних различны.
'''

file = open('k8-2.txt')
data = file.read()
file.close()
count = 0
max_count = 0
for i in range(1, len(data) - 1):
    if data[i] != data[i + 1]:
        count += 1
        continue
    elif max_count < count:
        max_count = count
    count = 1
print('6.', max_count)

'-------------------------------------------------------------------------------------------------------------------'

'''
159) Текстовый файл 24-157.txt содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ,
который чаще всего встречается в файле между двумя одинаковыми символами. Например, в тексте CCBAABABCBC есть
комбинации ABA, BAB, BCB и CBC. Чаще всего – 2 раза – между двумя одинаковыми символами стоит B, в ответе для этого
случая надо написать B2 (без пробелов и других разделителей). Если таких символов несколько, выведите тот, который
стоит раньше в алфавите.
'''

file = open('24-157.txt')
data = file.read()
file.close()
chars = {}
for i in range(65, 91):
    chars[chr(i)] = 0

for i in range(1, len(data) - 1):
    if data[i - 1] == data[i + 1]:
        chars[data[i]] += 1

max_value = max(list(chars.values()))

max_char = ''
for char in chars:
    if chars[char] == max_value:
        max_char = char
        break

print(f'159. {max_char}{max_value}')

'''
Ответы:   1. 1
          2. 11
          3. 95
          4. 891
          5. V 8
          6. 166
          159. W1608
'''

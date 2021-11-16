'''159)	Текстовый файл 24-157.txt содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ,
который чаще всего встречается в файле между двумя одинаковыми символами. Например, в тексте CCBAABABCBC есть
комбинации ABA, BAB, BCB и CBC. Чаще всего – 2 раза – между двумя одинаковыми символами стоит B, в ответе для этого
случая надо написать B2 (без пробелов и других разделителей). Если таких символов несколько, выведите тот, который
стоит раньше в алфавите.'''

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

print(f'{max_char}{max_value}')

string = input()
spaces = 0
numbers = 0
english_letter = 0
russian_letter = 0
symbols = 0
for char in string:
    if char == ' ':
        spaces += 1
    elif 48 <= ord(char) <= 57:
        numbers += 1
    elif 65 <= ord(char) <= 90 or \
            97 <= ord(char) <= 122:
        english_letter += 1
    elif 1040 <= ord(char) <= 1103 or \
            ord(char) == 1025 or ord(char) == 1105:
        russian_letter += 1
    else:
        symbols += 1
print('Пробелов:', spaces)
print('Цифр:', numbers)
print('Английских букв:', english_letter)
print('Русских букв:', russian_letter)
print('Остальных символов:', symbols)

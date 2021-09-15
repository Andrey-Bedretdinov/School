def is_space(symbol):
    if symbol == ' ':
        return True
    return False


def is_number(symbol):
    if '0' <= symbol <= '9':
        return True
    return False


def is_eng_letter(symbol):
    if 'A' <= symbol <= 'Z' or 'a' <= symbol <= 'z':
        return True
    return False


def is_rus_letter(symbol):
    if 'А' <= symbol <= 'я' or symbol == 'Ё' or symbol == 'ё':
        return True
    return False


string = input()
spaces = 0
numbers = 0
english_letters = 0
russian_letters = 0
symbols = 0
for char in string:
    if is_space(char):
        spaces += 1
    elif is_number(char):
        numbers += 1
    elif is_eng_letter(char):
        english_letters += 1
    elif is_rus_letter(char):
        russian_letters += 1
    else:
        symbols += 1
print('Пробелов:', spaces)
print('Цифр:', numbers)
print('Английских букв:', english_letters)
print('Русских букв:', russian_letters)
print('Остальных символов:', symbols)

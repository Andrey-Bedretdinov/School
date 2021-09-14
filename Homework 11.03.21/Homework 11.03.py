def is_digit(string):
    for char in string:
        if '0' <= char <= '9':
            continue
        return False
    return True


def is_alpha(string):
    for char in string:
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or 'А' <= char <= 'я' or \
                char == 'Ё' or char == 'ё':
            continue
        return False
    return True


def is_lower(string):
    for char in string:
        if 'a' <= char <= 'z' or 'а' <= char <= 'я' or char == 'ё':
            continue
        return False
    return True


def is_space(string):
    for char in string:
        if char == ' ' or char == '\f' or char == '\n' or char == '\r' or \
                char == '\t' or char == '\v':
            continue
        return False
    return True


def index(string, symb):
    i = 0
    for char in string:
        if char == symb:
            return i
        i += 1
    return -1


a = input('\nВведите строку: ')
if is_digit(a):
    print('Строка состоит исключительно из цифр')
if is_lower(a):
    print('Строка состоит исключительно из букв руссского или английского '
          'алфавита нижнего регистра')
elif is_alpha(a):
    print('Строка состоит исключительно из букв русского или английского '
          'алфавита')
if is_space(a):
    print('Строка состоит исключительно из невидимых символов')
print('-----------------------------------------------------------------------')
a = input('Введите строку, а затем символ, индекс которого нужно узнать:\n')
b = input()
print('Индекс данного символа: {0}'.format(index(a, b)))

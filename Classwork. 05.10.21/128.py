string = '2' * 3 + '5' * 18
while '222' in string or '888' in string:
    while '555' in string:
        string = string.replace('555', '8', 1)
    if '222' in string:
        string = string.replace('222', '8', 1)
    else:
        string = string.replace('888', '2', 1)
print(string)

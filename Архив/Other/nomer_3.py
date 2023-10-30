def f (a):
    if a >= 1 and a <= 9:
        if a == 1:
            print('один')
        if a == 2:
            print('два')
        if a == 3:
            print('три')
        if a == 4:
            print('четыре')
        if a == 5:
            print('пять')
        if a == 6:
            print('шесть')
        if a == 7:
            print('семь')
        if a == 8:
            print('восемь')
        if a == 9:
            print('девять')
    else:
        if a >= 10 and a <= 19:
            if a == 10:
                print('десять')
            if a == 11:
                print('одинадцать')
            if a == 12:
                print('двенадцать')
            if a == 13:
                print('тринадцать')
            if a == 14:
                print('четырнадцать')
            if a == 15:
                print('пятнадцать')
            if a == 16:
                print('шестнадцать')
            if a == 17:
                print('семнадцать')
            if a == 18:
                print('восемнадцать')
            if a == 19:
                print('девятнадцать')
        else:
            x = a // 10
            y = a % 10
            if x >= 2 and x <= 10:
                if x == 2:
                    print('двадцать')
                if x == 3:
                    print('тридцать')
                if x == 4:
                    print('сорок')
                if x == 5:
                    print('пятьдесят')
                if x == 6:
                    print('шесдесят')
                if x == 7:
                    print('семьдесят')
                if x == 8:
                    print('восемьдесят')
                if x == 9:
                    print('девяносто')
                if x == 10:
                    print('сто')
                if y == 1:
                    print('один')
                if y == 2:
                    print('два')
                if y == 3:
                    print('три')
                if y == 4:
                    print('четыре')
                if y == 5:
                    print('пять')
                if y == 6:
                    print('шесть')
                if y == 7:
                    print('семь')
                if y == 8:
                    print('восемь')
                if y == 9:
                    print('девять')


for i in range(1, 101):
    print(f'\n{i}: ')
    f(i)
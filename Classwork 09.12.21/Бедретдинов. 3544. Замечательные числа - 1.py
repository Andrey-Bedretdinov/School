for number in range(10, 100):
    if number == 2 * (number // 10) * (number % 10):
        print(number)

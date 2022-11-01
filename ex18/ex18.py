def sort():
    value1 = input('Insert number1: ')
    value2 = input('insert number2: ')
    value3 = input('Insert number3: ')

    while True:
        if value1 > value2 and value1 < value3:
            print(value2)
        elif value2 > value1 and value2 < value3:
            print(value1)
        else:
            print(value3)
        break

sort()
def copy_list():
    string = input('Insert string: ')
    number = int(input('Insert number: '))

    if number < 0:
        print('Invalid number!')
    elif number < 2:
        print(string[:2] * 2)
    else:
        print(string[:2] * number)

copy_list()
def odd_even():
    value = int(input('Enter number: '))

    if value % 2 == 0:
        print(f'Number {value} is even.')
    else:
        print(f'Number {value} is odd.')

odd_even()
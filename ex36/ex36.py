def if_integer(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        print("Input must be integer")
    else:
        print(x + y)
        
if_integer(2, 4)
if_integer(2.00, 123.12312)
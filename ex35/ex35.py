def equal():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    
    if x == y or x - y == 5 or x + y == 5:
        return True
    else:
        return False
    
print(equal())

def sum_tree():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = int(input("Third number: "))
    
    if x == y or x == z or y == z:
        print("Two or more numbers are equal so the result is: ", 0)
    else:
        print("Sum of numbers: ", x + y + z)
        
sum_tree()
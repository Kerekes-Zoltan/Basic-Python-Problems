
def sum_numbers():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    
    sum = x + y
    if sum in range(15, 20):
        print(20)
    else:
        print(sum)
        
sum_numbers()
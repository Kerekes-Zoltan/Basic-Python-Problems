def lcm():
    x = int(input("Insert first number: "))
    y = int(input("Insert second number: "))
    
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if z % x == 0 and z % y == 0:
            lcm = z
            break
        z += 1
    print(lcm)

lcm()
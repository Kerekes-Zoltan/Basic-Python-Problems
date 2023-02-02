def gcd(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y

print("GCD of 12 and 17: ", gcd(12, 17))
print("GCD of 4 and 6: ", gcd(4, 6))
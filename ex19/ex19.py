def pow_function(value):
    n, tmp, i = 2, 2, 2

    while True:
        if str(tmp) in value:
            i += 1
            tmp = pow(n, i)
        else:
            break

    return i - 1

print(pow_function('2481632'))
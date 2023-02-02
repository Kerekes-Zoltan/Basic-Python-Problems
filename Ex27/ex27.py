def concatenate(list):
    output = ''
    for i in list:
        output += str(i)
    return output

print(concatenate([1, 2, 42, 2]))
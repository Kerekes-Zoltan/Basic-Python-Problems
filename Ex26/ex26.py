def histogram(lista):
    for n in lista:
        output = ''
        cnt = n
        while (cnt > 0):
            output += '@'
            cnt = cnt - 1
        print(output)
        
histogram([2, 3, 6, 5])
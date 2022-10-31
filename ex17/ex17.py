from itertools import product


def strobogrammatic_pairs_of_n():

    strobogrammatic_pairs = {
    "1":"1",
    "6":"9",
    "8":"8",
    "9":"6",
    }
    n = int(input("Insert number: "))
    print("The list of strobogrammatic numbers of with %d digits are:"%n)

    for x in product("".join(strobogrammatic_pairs.keys()), repeat = n):
        x = ''.join(x)
        s = ''
        for y in reversed(x):
            s += strobogrammatic_pairs[y]
            if x == s:
                print(x)

strobogrammatic_pairs_of_n()
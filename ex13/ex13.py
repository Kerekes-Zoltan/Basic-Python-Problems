def combinations():
    digits = input("Enter two values between 1 - 9.\t")
    if digits == "":
        return []
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    c1 = string_maps[digits[0]]
    c2 = string_maps[digits[1]]
    c3 = []
    for i in c1:
        for j in c2:
            c3.append("{}{}".format(i,j))
    return c3

print(combinations())
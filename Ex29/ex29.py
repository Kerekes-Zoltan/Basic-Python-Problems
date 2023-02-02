color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def check_color():
    for i in color_list_1:
        if i not in color_list_2:
            print(i)
            
check_color()

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(set([i for i in color_list_1 if i not in color_list_2]))
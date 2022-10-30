def describe():
    method = input("Enter a method you want to know more about.\t")
    method_doc = method + ".__doc__"
    try:
        eval(method_doc)
    except:
        print("{} is not a built-in Python function or method!".format(method))
    else:
        method_info = eval(method_doc)
        print(method_info)

describe()
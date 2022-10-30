value = input("Filename: ")

f_extension = value.split('.')

print('Extension of file is: ' + repr(f_extension[-1]))
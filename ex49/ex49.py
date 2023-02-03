from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('Documents\Python\Basic-Python-Problems') if isfile(join('Documents\Python\Basic-Python-Problems', f))]
print(files_list)
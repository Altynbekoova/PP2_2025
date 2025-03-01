import os

path = '/Users/admin/Documents/Programming Principles/PP2_works/w7'

my_list = os.listdir(path)

print('Only directories: ')


for element in my_list:
    full_path = os.path.join(path, element)
    if os.path.isdir(full_path):
        print(element)

print('-----------------------')

print('Only files: ')

for element in my_list:
    full_path = os.path.join(path, element)
    if os.path.isfile(full_path):
        print(element)


print('-----------------------')

print('Directories and files: ')

for element in my_list: 
    print(element)
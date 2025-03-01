import os

my_list = ['1. apple', '2. banana', '3. cherry', '4. mango']

file_path = '/Users/admin/Documents/Programming Principles/PP2_works/w7/daf/sample.txt'

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, 'w') as my_file:
    my_file.writelines(fruit + '\n' for fruit in my_list)

print("List successfully written to file.")
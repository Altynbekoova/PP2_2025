import os

path = '/Users/admin/Documents/Programming Principles/PP2_works/w7'

if os.path.exists(path):
    print("Path exists!")
    print("Filename:", os.path.basename(path))  
    print("Directory:", os.path.dirname(path))  
else:
    print("Path does not exist.")


import os

path = '/Users/admin/Documents/Programming Principles/PP2_works/w7/daf/sample.txt'

if os.path.exists(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
    else: 
        print('File is not accessible')
else:
    print('File does not exist')
    

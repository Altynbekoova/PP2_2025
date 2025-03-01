with open('/Users/admin/Documents/Programming Principles/PP2_works/w7/daf/text.txt', 'r') as my_file_1:
    with open('sample_2.txt', 'w') as my_file_2:
        content = my_file_1.read()
        my_file_2.write(content)
        


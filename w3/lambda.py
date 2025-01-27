
add = lambda x, y: x + y
print(add(3, 5))  # 8

def multiplier(n):
    return lambda x: x * n

double = multiplier(2) 
triple = multiplier(3)  

print(double(5))  #  10
print(triple(5))  #  15


data = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [(2, 'a'), (1, 'b'), (3, 'c')]
def number(n):
    for i in range(n, -1, -1):
        yield i
        
n = int(input("enter: "))
for i in number(n):
    print(i)
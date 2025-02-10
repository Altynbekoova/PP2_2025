def num(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n =int(input("enter: "))
for i in num(n):
    print(i, end = " ") 
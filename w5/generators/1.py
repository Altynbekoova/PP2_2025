def square(N):
    for i in range(N + 1):
        yield i ** 2  


N = int(input("Enter N: "))
for sq in square(N):
    print(sq, end=" ")  
def even(N):
    for i in range (N+1):
        if i % 2 == 0:
            yield i
            
N = int(input("enter N: "))
for num in even(N):
    print(num, end = " ")
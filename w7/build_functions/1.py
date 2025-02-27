from functools import reduce

num = list(map(int,input().split()))

a = reduce(lambda x, y: x*y, num)
print(a)




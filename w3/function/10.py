def unique(nums):
    list = []
    
    for num in nums:
        if num not in list:
            list.append(num)
    return list

nums = list(map(int,input().split()))
print(unique(nums))
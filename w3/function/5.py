def permute(s, result = ""):
    if len(s) == 0:
        return [result]
    
    permutations = []

    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        permutations += permute(rest, result + ch)
    return permutations

s = input()
print(permute(s) , len(permute(s)))
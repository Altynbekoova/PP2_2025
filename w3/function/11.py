def palindrome(s):
    
    return s == s[::-1]

s = input()


if palindrome(s):
    print("palindrome")
else:
    print("no")
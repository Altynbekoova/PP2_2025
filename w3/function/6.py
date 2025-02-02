def reverse(str):
    words = str.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

str = input()

print(reverse(str))
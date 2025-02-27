st = input()
up_c = 0
low_c = 0

for i in range(len(st)):
    if st[i].isupper():
        up_c += 1
    elif st[i].islower():
        low_c += 1

print(up_c, low_c)  
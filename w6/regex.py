import re

#1
import re
text=input()
if re.search("a+b*",text):
    print ("True")
else:
    print("False")

print("1---------------------------------------")
#2
text=input()
if re.search("a+b{2,3}$",text):
    print ("True")
else:
    print("False")
print("2---------------------------------------")

#3
text=input()
if re.search("[a-z]+(_[a-z]+)",text):
    print ("True")
else:
    print("False")
print("3---------------------------------------")

#4
text=input()
if re.search("[A-Z]+([a-z]+)",text):
    print ("True")
else:
    print("False")
print("4---------------------------------------")

#5
text=input()
if re.search("a+[a-z]*b+",text):
    print ("True")
else:
    print("False")
print("5---------------------------------------")

#6
text=input()
new_text = re.sub(r"[\s,\.]", ":", text)
print(new_text)
print("6---------------------------------------")


#7
a=input()
new = ""
i=0
while i<len(a):
    if a[i] == "_":
        new += a[i + 1].upper()
        a = a[:i] + a[i+1:]
    else:
        new += a[i]
    i+=1
print(new)
print("7---------------------------------------")


#8
a=input()
result = re.findall(r'[a-z]+|[A-Z][a-z]*', a)
print(result)
print("8---------------------------------------")


#9
a = input()


result = re.sub(r'([a-z])([A-Z])', r'\1 \2', a)

print(result)
print("9---------------------------------------")


#10
a=input()
i=0
result=""
while i<len(a):
    if (a[i].isupper()):
        result+="_"
        result+=a[i].lower()
    else:
        result+=a[i]
    i+=1
print(result) 
print("10---------------------------------------") 
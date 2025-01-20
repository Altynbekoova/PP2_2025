# create distionaries 
person = {
    "name": "Aru",
    "age": 17,
    "city": "Almaty"
}
print(person)

# access to values
print(person["name"])  # Аru

# change the values
person["age"] = 18
print(person)

# print
for key, value in person.items():
    print(key, ":", value)

students = {"Аmanda": 90, "Lenda": 85, "Rose": 75}

for name, grade in students.items():
    if grade >= 90:
        print(name, "got an A")
    elif grade >= 70:
        print(name, "got a B")
    else:
        print(name, "нету стипендий")
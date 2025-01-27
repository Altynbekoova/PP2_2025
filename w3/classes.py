class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."




person1 = Person("Nikita", 25)
person2 = Person("Beisenbek", 30)

print(person1.greet())  
print(person2.greet())  

class Calculator:
    def __init__(self):
        self.operations = {
            "add": lambda x, y: x + y,
            "subtract": lambda x, y: x - y,
            "multiply": lambda x, y: x * y,
            "divide": lambda x, y: x / y if y != 0 else "Division by zero!"
        }

    def calculate(self, operation, x, y):
        if operation in self.operations:
            return self.operations[operation](x, y)
        return "Invalid operation"



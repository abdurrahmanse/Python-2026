# attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Abdur Rahman", 30)
print(person1.name)  # Output: Abdur Rahman
print(person1.age)   # Output: 30
# Output: Hello, my name is Abdur Rahman and I am 30 years old.
person1.say_hello()

person2 = Person("akaid", 25)
print(person2.name)  # Output: akaid
print(person2.age)   # Output: 25
person2.say_hello()  # Output: Hello, my name is akaid and I am 25 years old.

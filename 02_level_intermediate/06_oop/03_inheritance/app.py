# inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.student_id = student_id

    def introduce(self):
        super().introduce()  # Call the parent class method
        print(f"I'm a student with ID: {self.student_id}.")


# Create an instance of Student
student = Student("Alice", 20, "S12345")
student.introduce()

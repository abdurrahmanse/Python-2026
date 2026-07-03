# String Methods example:

name = "Alice"
print(name.upper())
print(name.lower())

# String slicing example:
greeting = "Hello, World!"
print(greeting[0:5])  # Output: Hello
print(greeting[7:12])  # Output: World

# String concatenation example:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# String formatting example:
age = 30
formatted_string = f"My name is {full_name} and I am {age} years old."
print(formatted_string)  # Output: My name is John Doe and I am 30 years old.

# String methods for checking content:
text = "Python is awesome!"
print(text.startswith("Python"))  # Output: True
print(text.endswith("awesome!"))  # Output: True

# String methods for finding and replacing:
sentence = "I love programming in Python."
print(sentence.find("Python"))  # Output: 24
new_sentence = sentence.replace("Python", "Java")
print(new_sentence)  # Output: I love programming in Java.


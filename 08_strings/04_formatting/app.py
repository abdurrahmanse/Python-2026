# String formatting in Python:

name = "Abdur Rahman"
print(f"Hello, {name}!")

# Using the format() method
age = 30
print("Hello, {}! You are {} years old.".format(name, age))

# Using the % operator
print("Hello, %s! You are %d years old." % (name, age))

# Using the format() method with named placeholders
print("Hello, {name}! You are {age} years old.".format(name=name, age=age))

# Using the format() method with positional placeholders
print("Hello, {0}! You are {1} years old.".format(name, age))

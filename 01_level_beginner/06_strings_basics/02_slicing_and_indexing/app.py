# slicing and indexing strings:

text = "Hello, World!"
print(text[0:5])  # Output: Hello

# Indexing
print(text[7])    # Output: W

# Slicing
print(text[7:12])  # Output: World

# Negative indexing
print(text[-6:-1])  # Output: World

# Slicing with step
print(text[::2])  # Output: Hlo ol!

# Slicing with negative step
print(text[::-1])  # Output: !dlroW ,olleH

# Slicing with start and end omitted
print(text[:5])   # Output: Hello

# Slicing with start omitted
print(text[7:])   # Output: World!

# lists example:

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Accessing elements
print(numbers[0])  # First element
print(numbers[-1])  # Last element

# Modifying elements
numbers[2] = 10
print(numbers)

# Adding elements
numbers.append(6)
print(numbers)

# Removing elements
numbers.remove(4)
print(numbers)

# Slicing
print(numbers[1:4])  # Elements from index 1 to 3

# Iterating through the list
for num in numbers:
    print(num)

# List comprehension
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

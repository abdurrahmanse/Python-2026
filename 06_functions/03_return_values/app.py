# Function Return Values
def add(x, y):
    return x + y


result = add(5, 3)
print(result)  # Output: 8

# Another example with a string


def greet(name):
    return f"Hello, {name}!"


greeting = greet("Abdur Rahman")
print(greeting)  # Output: Hello, Abdur Rahman!

# Example with a list


def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = get_even_numbers(numbers_list)
print(even_numbers)  # Output: [2, 4, 6]

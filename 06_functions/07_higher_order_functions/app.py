# Higher order fuctions example:

def apply_operation(x, y, operation):
    return operation(x, y)

# Example usage:


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)
print("Addition Result:", result1)  # Output: Addition Result: 8
print("Multiplication Result:", result2)  # Output: Multiplication Result: 15

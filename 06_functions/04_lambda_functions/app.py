# lamda function
from functools import reduce


def add(x, y):
    return x + y


print(add(5, 3))
# lambda function
def add_lambda(x, y): return x + y


print(add_lambda(5, 3))
# lambda function with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)
# lambda function with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# lambda function with reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

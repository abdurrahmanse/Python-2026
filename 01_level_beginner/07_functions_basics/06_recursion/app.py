# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

# Recursive function to calculate Fibonacci sequence


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))

# Recursive function to calculate the greatest common divisor (GCD)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))

# Recursive function to calculate the power of a number


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


print(power(2, 5))

# Recursive function to calculate the sum of a list


def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


print(sum_list([1, 2, 3, 4, 5]))

# Recursive function to reverse a string


def reverse_string(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


print(reverse_string("Hello, World!"))


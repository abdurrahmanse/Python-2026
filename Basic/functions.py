# numbers = [0, 1, 2, 1, 45, 556, 100]

def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2))

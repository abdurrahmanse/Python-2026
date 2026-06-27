# nested data structures example:

# a list of dictionaries
students = [
    {"name": "Alice", "age": 20, "grades": [90, 85, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 82, 88]},
    {"name": "Charlie", "age": 19, "grades": [95, 91, 89]}
]

# a dictionary of lists
courses = {
    "Math": ["Alice", "Bob"],
    "Science": ["Alice", "Charlie"],
    "History": ["Bob", "Charlie"]
}

# a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# a dictionary of dictionaries
library = {
    "Fiction": {
        "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925},
        "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960}
    },
    "Non-Fiction": {
        "Sapiens": {"author": "Yuval Noah Harari", "year": 2011},
        "Educated": {"author": "Tara Westover", "year": 2018}
    }
}

# accessing nested data structures
print(students[0]["name"])  # Output: Alice
print(courses["Math"])  # Output: ['Alice', 'Bob']
print(matrix[1][2])  # Output: 6
print(library["Fiction"]["The Great Gatsby"]
      ["author"])  # Output: F. Scott Fitzgerald

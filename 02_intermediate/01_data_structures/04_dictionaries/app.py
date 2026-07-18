# dictionaries example:

student = {
    "name": "Abdur Rahman",
    "age": 20,
    "major": "Computer Science"
}

# print the dictionary
print(student)

# access the value of a key
print(student["name"])

# add a new key-value pair to the dictionary
student["gpa"] = 3.8
print(student)


# update the value of an existing key
student["age"] = 21
print(student)

# remove a key-value pair from the dictionary
del student["major"]
print(student)


# get the length of the dictionary
print(len(student))

# Logical operators: and, or, not
a = True
b = False

print("a and b :", a and b)  # False
print("a or b  :", a or b)   # True
print("not a   :", not a)    # False

# Practical use in conditions
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

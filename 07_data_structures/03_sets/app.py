# set example:

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding an element to a set
my_set.add(6)
print(my_set)

# Removing an element from a set
my_set.remove(3)
print(my_set)

# Checking if an element is in a set
print(4 in my_set)  # True

# Iterating through a set
for item in my_set:
    print(item)

# Set operations:
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union
union_set = set_a.union(set_b)
print(union_set)  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # {3}

# Difference
difference_set = set_a.difference(set_b)
print(difference_set)  # {1, 2}

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # {1, 2, 4, 5}

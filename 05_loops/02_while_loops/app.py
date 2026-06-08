# while loops example:

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# while loops with else:
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print("Counter is no longer less than 5.")

# while loops with break:
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break

# while loops with continue:
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)

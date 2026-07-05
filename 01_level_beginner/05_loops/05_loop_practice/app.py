# loop practice

loop = 0
while loop < 5:
    print("Loop iteration:", loop)
    loop += 1

for i in range(5):
    print("For loop iteration:", i)
# nested loops
for i in range(3):
    for j in range(2):
        print(f"Outer loop: {i}, Inner loop: {j}")
# loop with else
for i in range(5):
    print("Loop iteration:", i)
else:
    print("Loop completed successfully!")
# break and continue
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue
    print("Current number:", i)

# output: 
# details of loop iterations, nested loops, and break/continue behavior.
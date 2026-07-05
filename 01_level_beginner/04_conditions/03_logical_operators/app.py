# logical operators
# and, or, not
# and - both conditions must be true
# or - at least one condition must be true
# not - negates the condition

# and example
age = 25
income = 50000
if age > 18 and income > 30000:
    print("You are eligible for the loan.")
# or example
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
# not example
is_raining = False
if not is_raining:
    print("It's a nice day outside!")
# combining logical operators
temperature = 30
if (temperature > 25 and day == "Saturday") or (temperature > 20 and day == "Sunday"):
    print("It's a great day for outdoor activities!")

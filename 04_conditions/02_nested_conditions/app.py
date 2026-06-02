# nested conditions
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
    if age < 13:
        print("You are a child.")
    else:
        print("You are a teenager.")
else:
    print("You are an adult.")
    if age < 65:
        print("You are a working adult.")
    else:
        print("You are a senior citizen.")

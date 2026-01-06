# def multiple(*list):
#     total = 1
#     for numbers in list:
#         total *= numbers
#     return total


# print(multiple(1, 2, 3, 4, 5))

def save_user(**user):
    print(user)


save_user(id=1, name='admin', roll=24204006)

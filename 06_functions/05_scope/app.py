# fucntions scope
def outer():
    x = 'local'
    print(x)


outer()

# global scope
y = 'global'


def outer():
    print(y)


outer()

# global scope
y = 'global'


def outer():
    y = 'local'
    print(y)


outer()
print(y)


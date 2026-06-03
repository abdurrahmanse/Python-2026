# context managers
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with File('example.txt', 'w') as f:
    f.write('Hello, World!')
# Output:
# The file 'example.txt' will be created with the content 'Hello, World!'

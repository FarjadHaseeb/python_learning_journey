class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            return False
        self.borrowed = True
        return True

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

library = [
    Book("Python Basics", "Student"),
    Book("Clean Code", "Robert Martin")
]

for book in library:
    print(book)

library[0].borrow()
print(library[0])

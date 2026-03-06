class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2026 - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"

# Example
b = Book("Python 101", "Jane Doe", "1234567890", 2020)
print(b.get_summary())
print(f"Book age: {b.get_age()} years")
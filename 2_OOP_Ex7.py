# Python Object-oriented-programming
# Class and object and function

from tabulate import tabulate


class Book:
    def __init__(self, title, author, ISBN, Is_available):
        self.Title = title
        self.Author = author
        self.Isbn = ISBN
        self.isavailable = Is_available

    def Display_info(self):
        return [self.Title, self.Author, self.Isbn, str(self.isavailable)]



class Library:
    def __init__(self):
        self.books = []

    def show_available_books(self):
        # Comprehension list  [____list____      for    _____item_____    in      ____iterable____ ]
        available_books = [book for book in self.books if book.isavailable]
        if available_books:
            print("Available Books:")
            table_header = ["Book Title", "Book Author", "Book ID", "Is Available"]
            table_data = [book.Display_info() for book in available_books]
            # for book in available_books:  book.Display_info()
            print(tabulate(table_data, headers=table_header, tablefmt="grid"))

        else:
            print("Available Books:")
            print("No books available in the library.")

    def show_borrowed_books(self):
        # Comprehension list  [____list____      for    _____item_____    in      ____iterable____ ]
        available_books = [book for book in self.books if not book.isavailable]
        if available_books:
            print("Unavailable Books:")
            table_header = ["Book Title", "Book Author", "Book ID", "Is Available"]
            table_data = [book.Display_info() for book in available_books]
            # for book in available_books:  book.Display_info()
            print(tabulate(table_data, headers=table_header, tablefmt="grid"))

        else:
            print("Unavailable Books:")
            print("No books unavailable in the library.")

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.Title}' added to library")

    def borrow_book(self, ISBN):
        for book in self.books:
            if book.Isbn == ISBN and book.isavailable:
                book.isavailable = False
                print(f"Book '{book.Title}' borrowed successfully.")
                return
        print("Book not available or ISBN not found.")

    def return_book(self, ISBN):
        for book in self.books:
            if book.Isbn == ISBN and not book.isavailable:
                book.isavailable = True
                print(f"Book '{book.Title}' returned successfully.")
                return
        print("Book not borrowed or ISBN not found.")


# Example of use
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", True)
book3 = Book("1984", "George Orwell", "978-0-452-28423-4", False)
book4 = Book("The Catcher ", "Salinger", "97876948-0", False)
book5 = Book("Mockingbird", "Lee", "978-0-8-4", True)
book6 = Book("1984", " Orwell", "978-28423-4", True)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

# View available book information
library.show_available_books()
# To borrow a book
library.borrow_book("978-0-316-76948-0")

# Show available books again
print("___________________________________________________")
library.show_available_books()
# Show unavailable books again
print("___________________________________________________")
library.show_borrowed_books()

# Return a book
library.return_book("978-0-316-76948-0")

# Show available books after return
library.show_available_books()
# Show unavailable books after return
library.show_borrowed_books()

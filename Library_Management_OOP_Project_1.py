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
        return [self.Title, self.Author, self.Isbn, self.isavailable]


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


class User:
    def __init__(self, name, user_id):
        self.Name = name
        self.User_id = user_id
        self.BooksBorrowed = []

    def Display_User_info(self):
        print(f"User Name : {self.Name}")
        print(f"User ID   : {self.User_id}")
        print(f"Books Borrowed : ")
        for book in self.BooksBorrowed:
            print(f" - {book.Display_info()[0]} by {book.Display_info()[1]}")

    def Borrow_book(self, book):
        if book.isavailable:
            self.BooksBorrowed.append(book)
            book.isavailable = False  # Update book availability
            print(f"{self.Name} borrowed the book: {book.Display_info()[0]} by {book.Display_info()[1]}")
        else:
            print(f"{self.Name} cannot borrow the book {book.Display_info()[0]} by {book.Display_info()[1]} as it is "
                  f"not available.")

    def return_book(self, book):
        if book in self.BooksBorrowed:
            self.BooksBorrowed.remove(book)
            book.isavailable = True
            print(f"{self.Name} returned the book: {book.Display_info()[0]} by {book.Display_info()[1]}")
        else:
            print(f"{self.Name} did not borrow the book: {book.Display_info()[0]} by {book.Display_info()[1]}")


class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()
        self.users = []

    def display_available_books(self):
        self.library.show_available_books()

    def display_unavailable_books(self):
        self.library.show_borrowed_books()

    def display_user_details(self):
        print("User Details:")
        for user in self.users:
            user.Display_User_info()
            print("-------------------------")

    def simulate_borrow_and_return(self, user_index, book_index):
        if 0 <= user_index < len(self.users) and 0 <= book_index < len(self.library.books):
            user = self.users[user_index]
            book = self.library.books[book_index]

            if book.isavailable:
                user.Borrow_book(book)
            else:
                user.return_book(book)
        else:
            print("Invalid user or book index.")


# Example of use
# Create a LibraryManagementSystem instance
library_system = LibraryManagementSystem()

# Add users
user1 = User("John Doe", 1)
user2 = User("laakroute amine", 2)
library_system.users.extend([user1, user2])

# Add books to the library
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", True)
book3 = Book("1984", "George Orwell", "978-0-452-28423-4", True)
book4 = Book("The Catcher ", "Salinger", "97876948-0", False)
book5 = Book("Mockingbird", "Lee", "978-0-8-4", True)
book6 = Book("1984", " Orwell", "978-28423-4", True)
library_system.library.books.extend([book1, book2, book3, book4, book5, book6])

# View the books available in the library
library_system.display_available_books()
# View the books unavailable in the library
library_system.display_unavailable_books()

# View details of all users
library_system.display_user_details()

# Simulate borrowing and returning books
library_system.simulate_borrow_and_return(user_index=0, book_index=0)
library_system.simulate_borrow_and_return(user_index=1, book_index=2)

# Show available and unavailable books and user details again after simulation
print("___________________________________________________")
library_system.display_available_books()
library_system.display_unavailable_books()
print("___________________________________________________")
library_system.display_user_details()

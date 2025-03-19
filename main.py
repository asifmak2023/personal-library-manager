class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by {author} added successfully!')

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for idx, book in enumerate(self.books, start=1):
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{idx}. {book.title} by {book.author} ({status})")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.borrow()
                print(f'You have borrowed "{title}".')
                return
        print(f'Sorry, "{title}" is either unavailable or already borrowed.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.return_book()
                print(f'You have returned "{title}".')
                return
        print(f'Error: "{title}" is not borrowed.')


def main():
    library = Library()

    while True:
        print("\nPersonal Library Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "2":
            library.list_books()
        elif choice == "3":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()

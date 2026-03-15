from library import Library
from storage import load_books, save_books
from utils import format_book

DATA_FILE = "books.json"


def display_books(library):
    books = library.list_books()

    if not books:
        print("No books in the library.")
        return

    for book in books:
        print(format_book(book))


def main():
    library = Library()

    books = load_books(DATA_FILE)
    library.books = books

    while True:
        print("\nLibrary Manager")
        print("1. List books")
        print("2. Add book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_books(library)

        elif choice == "2":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))

            library.add_book(title, author, year)
            save_books(DATA_FILE, library.books)

        elif choice == "3":
            title = input("Title to borrow: ")

            if library.borrow_book(title):
                print("Book borrowed.")
                save_books(DATA_FILE, library.books)
            else:
                print("Book not available.")

        elif choice == "4":
            title = input("Title to return: ")

            if library.return_book(title):
                print("Book returned.")
                save_books(DATA_FILE, library.books)
            else:
                print("Book not found or already available.")

        elif choice == "5":
            save_books(DATA_FILE, library.books)
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
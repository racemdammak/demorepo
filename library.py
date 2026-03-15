from utils import normalize_title, normalize_author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {
            "title": normalize_title(title),
            "author": normalize_author(author),
            "year": year,
            "available": True
        }

        self.books.append(book)

    def list_books(self):
        return self.books

    def find_book(self, title):
        normalized = normalize_title(title)

        for book in self.books:
            if book["title"] == normalized:
                return book

        return None

    def borrow_book(self, title):
        book = self.find_book(title)

        if book and book["available"]:
            book["available"] = False
            return True

        return False

    def return_book(self, title):
        book = self.find_book(title)

        if book and not book["available"]:
            book["available"] = True
            return True

        return False
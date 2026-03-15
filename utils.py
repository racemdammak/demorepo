def normalize_title(title):
    """
    Normalize book titles for consistent storage.
    """
    return title.strip().title()


def normalize_author(author):
    """
    Normalize author names.
    """
    return author.strip().title()


def format_book(book):
    """
    Format a book for display.
    """
    status = "Available" if book["available"] else "Borrowed"
    return f"{book['title']} by {book['author']} ({book['year']}) - {status}"
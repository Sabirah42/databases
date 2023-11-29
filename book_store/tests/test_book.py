from lib.book import *

"""
Check that Book constructs with id, title, and author_name
"""

def test_book_constructs():
    book = Book(1, "Pride and Prejudice", "Jane Austen")

    assert book.id == 1
    assert book.title == "Pride and Prejudice"
    assert book.author_name == "Jane Austen"

from lib.book_repository import *

"""
Book Repository #all function
Returns a llist of Book objects
"""

def test_book_repository_all_returns_all_books(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repository = BookRepository(db_connection)

    books = repository.all()

    assert len(books) == 5

    assert books[0].id ==  1
    assert books[0].title ==  'Nineteen Eighty-Four'
    assert books[0].author_name ==  'George Orwell'

    assert books[1].id ==  2
    assert books[1].title ==  'Mrs Dalloway'
    assert books[1].author_name ==  'Virginia Woolf'

    assert books[2].id ==  3
    assert books[2].title ==  'Emma'
    assert books[2].author_name ==  'Jane Austen'

    assert books[3].id ==  4
    assert books[3].title ==  'Dracula'
    assert books[3].author_name ==  'Bram Stoker'

    assert books[4].id ==  5
    assert books[4].title ==  'The Age of Innocence'
    assert books[4].author_name ==  'Edith Wharton'
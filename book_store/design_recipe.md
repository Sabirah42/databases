# Bookstore Model and Repository Classes Design Recipe

## 1. Design and create the Table

Tables already designed
```

## 2. Create Test SQL seeds

Seeds already created

Need to run:
```bash
psql -h 127.0.0.1 book_store_2023 < seeds_book_store.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():
    # Selecting all records
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns a list of Book objects.
 
```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all books

repo = BookRepository()

books = repo.all()

len(books) # =>  5

books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'

books[1].id # =>  2
books[1].title # =>  'Mrs Dalloway'
books[1].author_name # =>  'Virginia Woolf'

books[2].id # =>  3
books[2].title # =>  'Emma'
books[2].author_name # =>  'Jane Austen'

books[3].id # =>  4
books[3].title # =>  'Dracula'
books[3].author_name # =>  'Bram Stoker'

books[4].id # =>  5
books[4].title # =>  'The Age of Innocence'
books[4].author_name # =>  'Edith Wharton'



## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.library import Library
from src.book import Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        lib = Library()
        book = Book("1984", "George Orwell", 1949)
        lib.add_book(book)
        self.assertEqual(len(library.get_books()), 1)

    def test_find_book(self):
        lib = Library()
        book = Book("Test", "Author", 2020)
        lib.add_book(book)
        found = lib.find_book("Test")
        self.assertIsNotNone(found)
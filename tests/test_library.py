import unittest
from src.library import Book, PrintedBook, EBook, User, Library, Librarian


class TestPrintedBook(unittest.TestCase):
    def test_printed_book_creation(self):
        pbook = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
        self.assertEqual(pbook.get_title(), "Война и мир")
        self.assertIsInstance(pbook, PrintedBook)

    def test_printed_book_repair(self):
        pbook = PrintedBook("Старая книга", "Автор", 1900, 300, "плохая")
        pbook.repair()


class TestEBook(unittest.TestCase):
    def test_ebook_creation(self):
        ebook = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
        self.assertEqual(ebook.get_title(), "Мастер и Маргарита")
        self.assertIsInstance(ebook, EBook)

    def test_ebook_download(self):
        ebook = EBook("Тестовая книга", "Тестовый автор", 2023, 2, "pdf")
        ebook.download()


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Анна")
        self.book = Book("Тестовая книга", "Автор", 2023)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Анна")

    def test_borrow_book(self):
        self.user.borrow(self.book)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Книга 1", "Автор 1", 2000)
        self.book2 = Book("Книга 2", "Автор 2", 2001)
        self.user = User("Иван")

    def test_add_book(self):
        self.library.add_book(self.book1)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.remove_book("Книга 1")

    def test_find_book(self):
        self.library.add_book(self.book1)
        found = self.library.find_book("Книга 1")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_title(), "Книга 1")


class TestLibrarian(unittest.TestCase):
    def test_librarian_creation(self):
        librarian = Librarian("Мария")
        self.assertEqual(librarian.name, "Мария")


if __name__ == '__main__':
    unittest.main()

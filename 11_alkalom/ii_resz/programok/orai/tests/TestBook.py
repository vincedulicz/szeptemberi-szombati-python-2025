import unittest
from orai.Book.Book import Book


class TestBook(unittest.TestCase):
    def test_book_init(self):
        book = Book("test title", author="test auth", year=2025, isbn="12345")
        self.assertEqual(book.title, "test title")
        self.assertEqual(book.author, "test auth")
        self.assertEqual(book.year, 2025)
        self.assertEqual(book.isbn, "12345")

    def test_to_dict(self):
        # TODO: setUp and tearDwon
        book = Book("test title", author="test auth", year=2025, isbn="12345")
        expected_dict = {
            "title": "test title",
            "author": "test auth",
            "year": 2025,
            "isbn": "12345"
        }
        self.assertEqual(book.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()

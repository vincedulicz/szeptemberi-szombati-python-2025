import json
import os.path
import unittest
from unittest.mock import patch

from orai.Library.Library import Library
from orai.Book.Book import Book


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = "test_books.json"
        with open(self.test_file, "w") as file:
            json.dump([], file)
        self.library = Library(self.test_file)
        self.book = Book(title="test book", author="author", year=2025, isbn="12345")

    def tearDown(self) -> None:
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.book = None

    def test_load_books_empty_file(self):
        self.assertEqual(len(self.library.books), 0)

    def test_add_book(self):
        self.library.add_book(book=self.book)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "test book")

    def test_remove_book(self):
        self.library.add_book(book=self.book)
        self.library.remove_book("12345")
        self.assertEqual(len(self.library.books), 0)

    def test_list_books(self):
        self.library.add_book(book=self.book)

        # with self.assertLogs() as captured:
        #     self.library.list_books()
        # self.assertIn("test book", captured.output[0])

        with patch("builtins.print") as mocked_print:
            self.library.list_books()
            mocked_print.assert_called_once_with("test book by author (2025)")

    def test_sort_books_by_year(self):
        # TODO: DRY
        book = Book(title="test book", author="author", year=2026, isbn="12346")
        self.library.add_book(book=self.book)
        self.library.add_book(book=book)
        self.library.sort_books_by_year()
        self.assertEqual(self.library.books[0].year, 2025)

    def test_get_books_by_author(self):
        # TODO: DRY
        book = Book(title="test book", author="author b", year=2026, isbn="12346")
        self.library.add_book(book=self.book)
        self.library.add_book(book=book)
        books_by_author = self.library.get_books_by_author("author")
        self.assertEqual(len(books_by_author), 1)
        self.assertEqual(books_by_author[0].author, "author")


if __name__ == "__main__":
    unittest.main()

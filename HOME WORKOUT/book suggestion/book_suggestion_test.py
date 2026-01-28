from unittest import TestCase
from book_suggestion_function import get_suggestion, remove_book, add_book, update_book, show_all_books

class TestBookSuggestion(TestCase):

    def test_that_book_suggestion_method_exists(self):
        given = ["Odils", "theirs"]
        when = get_suggestion(given)
        expected = ["Odils"]
        self.assertTrue(when, expected)

    def test_that_remove_book_works(self):
        when = remove_book(["Odili"], "Odili")
        expected = []
        self.assertEqual(when, expected)

    def test_that_add_book_works(self):
        when = add_book([], "Ejeh")
        expected = ["Ejeh"]
        self.assertEqual(when,expected)

    def test_that_update_book_works(self):
        when = update_book(["Odili", "Ejeh"], "Ejeh", "Flash")
        expected = ["Odili", "Flash"]
        self.assertEqual(when, expected)

    def test_that_show_all_books_works(self):
        when = show_all_books(["Odili", "Flash"])
        expected = ["Odili", "Flash"]
        self.assertEqual(when,expected)

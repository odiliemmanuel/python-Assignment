import unittest

from me import square

class Square(unittest.TestCase):

    def test_method_exists(self):
        self.assertTrue(square)

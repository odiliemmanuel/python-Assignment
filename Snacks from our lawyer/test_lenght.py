import unittest

from lenght import lenght_of_a_list

class TestLengthNumber(unittest.TestCase):
    def test_that_method_exists(self):
        self.assertTrue(lenght_of_a_list)

    def test_that_lenght_is_correct(self):
        given =  [10, 20, 30, 40]
        when = lenght_of_a_list([10, 20, 30, 40])
        expected = 7
        self.assertEqual(when, expected)

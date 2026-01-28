import unittest

from cube import test_cube

class TestCube(unittest.TestCase):

    def test_that_method_exists(self):
        self.assertTrue(test_cube)

    def test_that_number_raised_to_3_is_correct(self):
        given = 4
        when = test_cube(4)
        expected = 64

        self.assertEqual(when, expected)

    def test_that_negative_numbers_return_correct_values_in_negative(self):
        given = -2
        when = test_cube(-2)
        expected = -8

        self.assertEqual(when, (-2 ** 3))


    def test_that_decimal_numbers_return_correct_values_in_decimal(self):
        given = 5.5
        when = test_cube(5.5)
     
        self.assertEqual(when,(5.5 ** 3))

    def test_that_percentage_value_returns_correct_values_in_decimal(self):
        given = 34/10
        when = test_cube(34/10)

        self.assertEqual(when,(34/10 ** 3))




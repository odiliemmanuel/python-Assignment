import unittest

from average import average_of_a_list

class TestAverage (unittest.TestCase):

    def test_that_method_exists(self):
        self.assertEqual(average_of_a_list)

    def test_that_average_is_correct(self):
        given = [10, 20, 30, 40, 50]
        when = average_of_a_list([10, 20, 30, 40, 50])
        expected = 30
    
        self.assertEqual(when, expected)

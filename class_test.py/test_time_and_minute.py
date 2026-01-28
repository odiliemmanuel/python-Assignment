#import unittest
#
#import time_right
#
#class TestTimeAndMinuteFunction(unittest.TestCase):
#    def test_that_is_Time_function_exist(self):
#        self.assertEqual(time_right.is_Time(130), (2, 10))
#
#    def test_that_is_Time_function_return_time_with_minutes_argument(self):
#        actual = function_snacks.is_Time(140)
#        expected = time
#        self.assertEqual(actual, expected)
#        actual = function_snacks.is_even(180)
#        expected = time
#        self.assertEqual(actual, expected)
#
#    def test_that_is_even_function_return_false_with_odd
#



import statistics

grades = [85, 93, 45, 89,85]

mean = statistics.mean(grades)

mode = statistics.mode(grades)

median = statistics.median(grades)

order = sorted(grades)

print(mean)

print(mode)

print(median)

print(order)

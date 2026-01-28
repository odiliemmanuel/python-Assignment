import unittest

from lenght import count_lenght_of_a_given_string

class TestLenght(unittest.TestCase):

    def test_that_method_exists(self):
        self.assertTrue(count_lenght_of_a_given_string)

    def test_that_input_is_a_string(self):
        given = "Odiliemmanuel"
        when = count_lenght_of_a_given_string("Odiliemmanuel")
        expected = 13
        self.assertEqual(when, expected)

    def test_that_string_is_of_acceptable_lenght(self):
        given = "ejeh"
        when = count_lenght_of_a_given_string("ejeh")
        bool_value = True
        if(when > 0):
            bool_value = True
        else:            
            bool_value  = False
        
        expected = len(given) > 0
        self.assertEqual(bool_value, expected)
         

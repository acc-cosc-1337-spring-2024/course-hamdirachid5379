import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_get_options_ratio_1(self):
        self.assertEqual(get_options_ratio(5, 20), .25)

    def test_get_options_ratio_2(self):
        self.assertEqual(get_options_ratio(10, 20), .5)

    def test_is_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating(.91), "Excellent")

    def test_is_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating (.85), "Very Good")

    def test_is_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating (.71), "Good")

    def test_is_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating (.66), "Needs Improvements")

    def test_is_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating (.45), "Unacceptable")

    def test_is_get_factorial_1(self):
        self.assertEqual(get_factorial(4), 24)

    def test_is_get_factorial_2(self):
        self.assertEqual(get_factorial(5), 120)

    def test_is_get_factorial_3(self):
        self.assertEqual(get_factorial(6), 720)

    def test_is_sum_of_odd_numbers_1(self):
        self.assertEqual(sum_odd_numbers(9), 25)
    
    def test_is_sum_of_odd_numbers_2(self):
        self.assertEqual(sum_odd_numbers(10), 25)
        

                                   
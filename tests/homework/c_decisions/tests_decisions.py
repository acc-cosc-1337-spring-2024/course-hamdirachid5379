import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

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
        

                                   
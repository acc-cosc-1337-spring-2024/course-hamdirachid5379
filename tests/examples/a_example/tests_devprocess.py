import unittest

from src.examples.a_example.devprocess import add_numbers, subtract_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):#create one test function that add_numbers works as expected
        self.assertEqual(2, add_numbers(1, 1))
        
    def test_subtract_numbers_1(self): # test function subtract in devprocess.py file
        self.assertEqual(5, (subtract_numbers(10, 5)))


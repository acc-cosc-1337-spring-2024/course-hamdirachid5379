import unittest

from src.examples.a_example.devprocess import add_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):#create one test function that add_numbers works as expected
        self.assertEqual(2, add_numbers(1, 2))


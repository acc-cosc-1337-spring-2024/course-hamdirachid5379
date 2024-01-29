from typing import Self
import unittest
from homework.b_in_proc_out.main import multiply_numbers

from src.examples.a_example.devprocess import add_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))
        
    def test_multiply_numbers_1(self):
         Self.assertEqual(multiply_numbers(5, 5), 25)


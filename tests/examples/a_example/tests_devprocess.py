import unittest


from src.examples.a_example.devprocess import add_numbers, floating_point_division, subtract_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):#create one test function that add_numbers works as expected
        self.assertEqual(2, add_numbers(1, 1))
        
    def test_subtract_numbers_1(self): # test function subtract in devprocess.py file
        self.assertEqual(5, (subtract_numbers(10, 5)))
    
    def test_floating_point_division_1(self): # test function floating division
        self.assertEqual((floating_point_division(5, 2), 2.5))
    
    def test_floating_point_division_2(self):
        self.assertEqual((floating_point_division(5, 2), 2.7))

    def test_floating_point_division_3(self):
        self.assertEqual((floating_point_division(20, 8), 2.5))

    

    


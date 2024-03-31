import unittest

from src.homework.i_dictionaries_and_sets import get_p_distance
from src.homework.i_dictionaries_and_sets import get_p_distance

class Test_Config(unittest.TestCase):

    #def test_configuration(self):
        #self.assertEqual(True, test_config())

    def test_add_inventory(self):
        widgets = {}
        self.assertEqual(widgets['widget1'], 10)
        self.assertEqual(widgets['widget1': 25], 35)
        self.assertEqual(widgets['widget1': -10], 25)

    def test_remove_inventory_widget(self):
        widgets = {}
        self.assertEqual(widgets['widget1'], 5)
        self.assertEqual(widgets['widget2'], 7)
        del (widgets['widget1'], 5)
        self.assertEqual(len [widgets], 1)
        
    

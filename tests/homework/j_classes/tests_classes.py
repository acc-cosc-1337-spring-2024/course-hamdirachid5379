#
import random
import unittest

from tests.homework.j_classes import tests_classes

class Test_config(unittest.TestCase):

    def test_get_rolled_value(self):
       self.assertEqual(random.randint(1, 1), 1)

    def test_get_rolled_value(self):
       self.assertEqual(random.randint(2, 2), 2)

    def test_get_rolled_value(self):
        self.assertEqual(random.randint(6, 6), 6)
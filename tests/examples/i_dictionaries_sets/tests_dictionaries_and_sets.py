import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
'''
    def test_dictionary_key_access(self):
        prog_langs= {'C++:1979', 'Java:1992', 'Python:1996', 'C#:2001'}
        self.assertEqual(prog_langs(['C++'], '1979'))
'''

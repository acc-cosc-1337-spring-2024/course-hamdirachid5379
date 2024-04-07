#test the sets
import unittest
from src.homework.i_dictionaries_sets.sets  import get_students_who_took_prog1_and_prog2,get_students_who_took_prog2_only, get_students_who_took_prog1_not_prog2,get_students_who_took_prog2_not_prog1



class Test_Config(unittest.TestCase):
 
    def test_get_students_who_took_prog1_and_prog2(self):
        prog1 =  set(['student1', 'student2', 'student3'])
        prog2 = set(['student3', 'student4', 'student5']) 
        self.assertEqual(prog1.union(prog2), {'student1', 'student2', 'student3', 'student4', 'student5'}) 

    def test_get_students_who_took_prog2_only(self):
        prog1 =  set(['student1', 'student2', 'student3'])
        prog2 = set(['student3', 'student4', 'student5']) 
        self.assertEqual(prog2.difference(prog1), {'student4','student5'})                           

    def test_get_students_who_took_prog1_not_prog2(self):
        prog1 =  set(['student1', 'student2', 'student3'])
        prog2 = set(['student3', 'student4', 'student5']) 
        self.assertEqual(prog1.difference(prog2), {'student1','student2'})

    def test_get_students_who_took_prog2_not_prog1(self):
        prog1 =  set(['student1', 'student2', 'student3'])
        prog2 = set(['student3', 'student4', 'student5']) 
        self.assertEqual(prog2.difference(prog1), {'student4','student5'}) 
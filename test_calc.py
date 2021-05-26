import unittest
import calc


class testCalc(unittest.TestCase):

    # 2 Test triple function to check input validation and calculations
    def test_triple_false(self): 
        self.assertEqual(calc.triple("shsh"), False, "Should be False")
    
    def test_triple(self): 
        self.assertEqual(calc.triple(2), 6, "Should be 6")

    # 2 Test cubed function to check input validation and calculations
    def test_cubed_false(self):
        self.assertEqual(calc.cubed("shhsh") , False, "Should be False")
    
    def test_cubed(self):
        self.assertEqual(calc.cubed(3) , 27, "Should be 27")

    # 3 Test addThen Cubed function to check input validation and calculations
    def test_addThenCubed_false(self):
        self.assertEqual(calc.addThenCubed("hsjj",6), False, "Should be False")

    def test_addThenCubed_false2(self):
        self.assertEqual(calc.addThenCubed(6, "hsjj"), False, "Should be False")
    
    def test_addThenCubed2(self):
        self.assertEqual(calc.addThenCubed(4, 6), 1000, "Should be 1000")
 
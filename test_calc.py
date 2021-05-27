import unittest
import calc


class testCalc(unittest.TestCase):

    #Test triple function to check input validation and calculations
    def test_triple(self): 
        self.assertEqual(calc.triple(2), 6, "Should be 6")

        self.assertRaises(ValueError, calc.triple, "2a")
        self.assertRaises(ValueError, calc.triple, 2.5)

    #Test cubed function to check input validation and calculations
    def test_cubed(self):
        self.assertEqual(calc.cubed(3) , 27, "Should be 27")

        self.assertRaises(ValueError, calc.cubed, "!")
        self.assertRaises(ValueError, calc.cubed, 2.5)

    #Test addThen Cubed function to check input validation and calculations
    def test_addThenCubed2(self):
        self.assertEqual(calc.addThenCubed(4, 6), 1000, "Should be 1000")

        self.assertRaises(ValueError, calc.addThenCubed, "gqyqwus", 2)
        self.assertRaises(ValueError, calc.addThenCubed, 4, "")
        self.assertRaises(ValueError, calc.addThenCubed, 2.5, 1)
        self.assertRaises(ValueError, calc.addThenCubed, 10, 2.5)
 
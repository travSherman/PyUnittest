import unittest
import MODULE


class testModule(unittest.TestCase):

    def test_triple(self):
        self.assertEqual(MODULE.triple(2), 6, "Should be 6")

    def test_cubed(self):
        self.assertEqual(MODULE.cubed(3) , 27, "Should be 27")

    def test_addThenCubed(self):
        self.assertEqual(MODULE.addThenCubed(4,6), 1000, "Should be 1000")
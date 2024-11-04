import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_zero_negative(self):
        self.assertEqual(self.calc.add(-6, 0), -6)

    def test_zero_negative(self):
        self.assertEqual(self.calc.add(-6, 0), -6)  

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 4), 2) 

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-4, -6), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
    
    def test_multiply_onenegative(self):
        self.assertEqual(self.calc.multiply(2, -5), -10)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_multiply_zero_negative(self):
        self.assertEqual(self.calc.multiply(0, -5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 2)

    def test_divide_equal(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4, 3), 1)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(4, 4), 0)




if __name__ == '__main__':
    unittest.main()
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test cases for the add method
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Normal case
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive
        self.assertEqual(self.calc.add(-2, -3), -5)  # Both negative
        self.assertEqual(self.calc.add(0, 0), 0)  # Edge case: both zero

    # Test cases for the subtract method
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Normal case
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Negative and positive
        self.assertEqual(self.calc.subtract(-3, -2), -1)  # Both negative
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Edge case: both zero

    # Test cases for the multiply method
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Normal case
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Negative and positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Both negative
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Edge case: zero

    # Test cases for the divide method
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Normal case
        self.assertEqual(self.calc.divide(-6, 2), -3)  # Negative and positive
        self.assertEqual(self.calc.divide(-6, -3), 2)  # Both negative
        self.assertEqual(self.calc.divide(0, 5), 0)  # Edge case: zero numerator
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero case
        self.assertIsNone(self.calc.divide(0, 0))  # Edge case: zero divided by zero

if __name__ == "__main__":
    unittest.main()

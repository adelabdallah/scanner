from unittest import TestCase

from scanner.poc.babysFirstUnitTest import BasicCalculator


class TestBasicCalculator(TestCase):

    def test_add(self):
        self.assertEqual(6, BasicCalculator.add(3, 3))
        self.assertEqual(7, BasicCalculator.add(10, -3))
        self.assertEqual(0, BasicCalculator.add(0, 0))
        self.assertEqual(-21, BasicCalculator.add(-7, -14))
        self.assertEqual(1.5, BasicCalculator.add(0.5, 1))
        self.assertEqual(100, BasicCalculator.add(100, 0))

    def test_subtract(self):
        self.assertEqual(6, BasicCalculator.subtract(7, 1))
        self.assertEqual(7, BasicCalculator.subtract(4, -3))
        self.assertEqual(0, BasicCalculator.subtract(0, 0))
        self.assertEqual(-21, BasicCalculator.subtract(-35, -14))
        self.assertEqual(1.5, BasicCalculator.subtract(2.5, 1))
        self.assertEqual(100, BasicCalculator.subtract(100, 0))

    def test_multiply(self):
        self.assertEqual(6, BasicCalculator.multiply(2, 3))
        self.assertEqual(7, BasicCalculator.multiply(7, 1))
        self.assertEqual(0, BasicCalculator.multiply(0, 1))
        self.assertEqual(-21, BasicCalculator.multiply(7, -3))
        self.assertEqual(1.5, BasicCalculator.multiply(1.5, 1))
        self.assertEqual(100, BasicCalculator.multiply(10, 10))

    def test_divide(self):
        self.assertEqual(6, BasicCalculator.divide(12, 2))
        self.assertEqual(7, BasicCalculator.divide(-21, -3))
        self.assertEqual(0, BasicCalculator.divide(0, 1))
        self.assertEqual(-21, BasicCalculator.divide(-21, 1))
        self.assertEqual(1.5, BasicCalculator.divide(3, 2))
        self.assertEqual(100, BasicCalculator.divide(300, 3))

    def test_exponent(self):
        self.assertEqual(1, BasicCalculator.exponent(3, 0))
        self.assertEqual(1, BasicCalculator.exponent(1, 27))
        self.assertEqual(0, BasicCalculator.exponent(0, 800))
        self.assertEqual(-21, BasicCalculator.exponent(-21, 1))
        self.assertEqual(8, BasicCalculator.exponent(2, 3))
        self.assertEqual(100, BasicCalculator.exponent(10, 2))

    def test_root(self):
        self.assertEqual(2, BasicCalculator.root(4, 2))
        self.assertEqual(3, BasicCalculator.root(27, 3))
        self.assertEqual(0, BasicCalculator.root(0, 800))
        self.assertEqual(2, BasicCalculator.root(8, 3))
        self.assertEqual(100, BasicCalculator.root(10000, 2))
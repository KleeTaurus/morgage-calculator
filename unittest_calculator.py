# -*- coding: utf-8 -*-
import unittest
from calculator import (ACMCalculator, ACPIMCalculator)


class MorgageCalculatorTest(unittest.TestCase):

    def testACM25Years(self):
        r = ACMCalculator(87 * 10000, 25, 4.9 / 100).calculate()

        self.assertEqual(r[11], 6334.08)
        self.assertEqual(r[23], 6191.98)
        self.assertEqual(r[149], 4699.93)

    def testACPIM25Years(self):
        r = ACPIMCalculator(87 * 10000, 25, 4.9 / 100).calculate()
        self.assertEqual(r, 5035.37)

    def testACPIM30Years(self):
        r = ACPIMCalculator(87 * 10000, 30, 4.9 / 100).calculate()
        self.assertEqual(r, 4617.32)


if __name__ == '__main__':
    unittest.main()

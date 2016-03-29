# -*- coding: utf-8 -*-
import unittest
from calculator import (ACCalculator, ACPICalculator)


class LoanCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.ac_calc = ACCalculator()
        self.acpi_calc = ACPICalculator()

    def test25YearsACLoan(self):
        total_loan = 87 * 10000
        years = 25
        annual_rate = 4.9 / 100

        repayments = self.ac_calc.calculate(
            total_loan, years, annual_rate)

        self.assertEqual(repayments[10], 6334.08)
        self.assertEqual(repayments[22], 6191.98)
        self.assertEqual(repayments[148], 4699.93)

    def test25YearsACPILoan(self):
        total_loan = 87 * 10000
        years = 25
        annual_rate = 4.9 / 100

        repayment = self.acpi_calc.calculate(
            total_loan, years, annual_rate)
        self.assertEqual(repayment, 5035.37)

    def test30YearsACPILoan(self):
        total_loan = 87 * 10000
        years = 30
        annual_rate = 4.9 / 100

        repayment = self.acpi_calc.calculate(
            total_loan, years, annual_rate)
        self.assertEqual(repayment, 4617.32)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
from __future__ import print_function
from calculator import ACMCalculator
from calculator import ACPIMCalculator

def calculate_with_ac_method():
    u"""采用等额本金还款法"""
    total_morgage = 100 * 10000  # 贷款总额 100 万
    years = 30                   # 贷款年限 30 年
    annual_rate = 4.9 / 100      # 年利率 4.9%

    calculator = ACMCalculator(total_morgage, years, annual_rate)
    monthly_repayments = calculator.calculate()
    print(u'等额本金每月还款额:')
    for x in monthly_repayments:
        if (x - 1) % 6 == 0:
            print()
        print('[%03d]: %.2f ' % (x, monthly_repayments[x]), end='')
    else:
        print('\n\n')

def calculate_with_acpi_method():
    u"""采用等额本息还款法"""
    total_morgage = 100 * 10000  # 贷款总额 100 万
    years = 30                   # 贷款年限 30 年
    annual_rate = 4.9 / 100      # 年利率 4.9%
    floating_rate = 1.1          # 利率上浮 10%

    calculator = ACPIMCalculator(total_morgage, years, annual_rate,
                                 floating_rate=floating_rate)
    monthly_repayment = calculator.calculate()
    print(u'等额本息每月还款额:')
    print('%.2f' % monthly_repayment)


calculate_with_ac_method()
calculate_with_acpi_method()

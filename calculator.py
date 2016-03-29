# -*- coding: utf-8 -*-
u"""房贷计算器.

支持 "等额本金" 和 "等额本息" 两种计算方式
"""


class ACCalculator(object):
    u"""等额本金(Average Capital)还款法."""

    @staticmethod
    def calculate_repayment_per_month(total_loan, months, monthly_rate, n):
        u"""计算第n月还款金额.

        :total_loan: 贷款总额(单位:元)
        :months: 贷款期限(月)
        :monthly_rate: 月利率
        :n: 第n月
        """
        capital_per_month = total_loan / months
        interest = (total_loan - (n - 1) * capital_per_month) * monthly_rate

        return round(capital_per_month + interest, 2)

    def calculate(self, total_loan, years, annual_rate, floating_rate=1.0):
        u"""计算每月还款金额.

        :total_loan: 贷款总额(单位:元)
        :years: 贷款期限(年)
        :annual_rate: 年利率
        :floating_rate: 浮动利率
        :return: 每月还款金额列表
        """
        months = years * 12
        monthly_rate = float(annual_rate * floating_rate) / 12

        repayment = list()
        for i in range(1, months + 1):
            repayment.append(self.calculate_repayment_per_month(
                total_loan, months, monthly_rate, i))

        return repayment


class ACPICalculator(object):
    u"""等额本息(Average Capital Plus Interest)还款法."""

    def calculate(self, total_loan, years, annual_rate, floating_rate=1.0):
        u"""计算每月还款金额, 采用等额本息还款法每月还款金额固定.

        :total_loan: 贷款总额(单位:元)
        :years: 贷款年限(年)
        :annual_rate: 年利率
        :floating_rate: 浮动利率
        :return: 每月还款金额
        """
        months = years * 12
        monthly_rate = float(annual_rate * floating_rate) / 12

        compound = (1 + monthly_rate) ** months
        repayment = (total_loan * monthly_rate * compound) / (compound - 1)
        return round(repayment, 2)

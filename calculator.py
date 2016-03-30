# -*- coding: utf-8 -*-
u"""房贷计算器.

支持 "等额本金" 和 "等额本息" 两种计算方式
"""


class MorgageCalculator(object):
    u"""房贷计算器基类."""

    def __init__(self, total_morgage, years, annual_rate, floating_rate=1.0):
        u"""初始化方法.

        :param total_morgage: 贷款总额 (单位:元)
        :param years: 贷款年限
        :param annual_rate: 年利率
        :param floating_rate: 浮动利率
        """
        self.total_morgage = total_morgage
        self.years = years
        self.annual_rate = annual_rate
        self.floating_rate = floating_rate

        self.months = years * 12
        self.monthly_rate = float(annual_rate * floating_rate) / 12

    def calculate(self):
        u"""根据不同贷款计算方法计算每月还款额."""
        raise NotImplementedError()


class ACMCalculator(MorgageCalculator):
    u"""等额本金(Average Capital)计算器."""

    def _calculate_monthly_repayment(self, n):
        u"""计算第n月还款金额.

        :param n: 第n月
        """
        capital = self.total_morgage / self.months
        interest = (self.total_morgage - (n - 1) * capital) * self.monthly_rate

        return capital + interest

    def calculate(self):
        u"""计算每月还款金额, 采用等额本金还款法每月还款金额不固定, 每月还款金额存入字典."""
        self.monthly_repayments = {}

        for i in range(1, self.months + 1):
            monthly_repayment = self._calculate_monthly_repayment(i)
            self.monthly_repayments[i] = round(monthly_repayment, 2)

        return self.monthly_repayments


class ACPIMCalculator(MorgageCalculator):
    u"""等额本息(Average Capital Plus Interest)计算器."""

    def calculate(self):
        u"""计算每月还款金额, 采用等额本息还款法每月还款金额固定."""
        compound = (1 + self.monthly_rate) ** self.months
        repayment = (self.total_morgage * self.monthly_rate * compound) / \
            (compound - 1)
        self.monthly_repayment = round(repayment, 2)

        return self.monthly_repayment

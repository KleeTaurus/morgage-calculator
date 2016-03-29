# 房贷计算器 (Python版)

该计算器支持等额本金 (Average Capital) 及等额本息 (Average Capitital Plus Interest) 两种计算方式。等额本金的方式还款，开始每月还款较多，之后逐月递减。等额本息的方式还款，每个月还款金额固定，但最后还的总利息相对较多。

**使用方法:**

```python
# 等额本金计算
from calculator import ACCalculator

ac_calc = ACCalculator()

total_loan = 87 * 10000
years = 25
annual_rate = 4.9 / 100

repayments = ac_calc.calculate(total_loan, years, annual_rate)

for x in repayments:
    print x
```

```python
# 等额本息计算
from calculator import ACPICalculator

acpi_calc = ACPICalculator()
total_loan = 87 * 10000
years = 25
annual_rate = 4.9 / 100

repayment = acpi_calc.calculate(total_loan, years, annual_rate)
print repayment
```

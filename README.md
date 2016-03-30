# 房贷还款计算器

## 概述

该计算器支持 **等额本金** (Average Capital) 及 **等额本息** (Average Capitital Plus Interest) 两种计算方式。采用 **等额本金** 的还款方式，开始每月还款较多，之后逐月递减。采用 **等额本息** 的还款方式，每月还款固定，但最后需要支付的总利息相对较多。

## 使用

#### 采用 "等额本金" 方法计算:

```python
from calculator import ACCalculator

ac_calc = ACCalculator()

total_loan = 87 * 10000
years = 25
annual_rate = 4.9 / 100

repayments = ac_calc.calculate(total_loan, years, annual_rate)

for x in repayments:
    print x
```

#### 采用 "等额本息" 方法计算:

```python
from calculator import ACPICalculator

acpi_calc = ACPICalculator()
total_loan = 87 * 10000
years = 25
annual_rate = 4.9 / 100

repayment = acpi_calc.calculate(total_loan, years, annual_rate)
print repayment
```

## 手机预览

请用微信扫码

![](./dist/example/snapshot/qrcode.png)

## License
The MIT License(http://opensource.org/licenses/MIT)
请自由地享受和参与开源

## 贡献

如果你有好的意见或建议，欢迎给我们提issue或pull request，为提升微信web体验贡献力量

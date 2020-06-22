"""
BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字

BMI < 18.5 体重偏轻
18.5 <= BMI < 24 体重正常
 BMI >= 24 体重偏重
设计一个BMI计算器吧，看看自己体重是否正常。

输入：身高、体重值

输出：BMI 指数、是否正常
"""
print('this is a BMI calculator\nplease input your information')
height = input('your height(meters):')
weight = input('your weight(kg):')
bmi = float(weight) / (float(height) ** 2)
if bmi < 18.5:
    print('you\'re too thin, you need to put on some weight')
elif bmi >= 24:
    print('you have to lose some weight to keep healthy')
else:
    print('you are totally healthy')

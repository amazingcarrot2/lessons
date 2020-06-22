# 1
money = 88
if money > 100:
    print('"rich"')
else:
    print('"poor"')

# BMI 计算器

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

'''
字符串拼接
'''
# 通过 % 将 name, age, code 拼接成一句话
# 输出 Crossin is 18, he writes Python.

name = 'Crossin'
age = 18
code = 'Python'
result = '%s is %d, he writes %s' % (name, age, code)
print(result)


'''
print()
'''
num1 = '3.3'
num2 = 2.5

# 将 num1 转换为浮点数
num1 = float(num1)

# 再和 num2 相加后输出
print(num1 + num2)

'''
bool类型转换
'''

bool(-123)      #T
bool(0)         #F
bool('abc')     #T
bool('False')   #T
bool('')        #F
bool([])        #F
bool({})        #F
bool([''])      #T
bool(None)      #F
print(bool('False'))
print(bool(''))
print(bool(['']))

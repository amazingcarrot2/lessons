# 基础版字符串的输出
num = 18
print('My age is ' + str(num))
print('My age is %d' % num)
print('Price is %f' % 4.99)
print('Price is %.2f' % 4.99)
name = 'Crossin'
print('%s is a good teacher.' % name)
print('Today is %s.' % 'Friday')
print("%s's score is %d" % ('Mike', 87))
name = 'Lily'
score = 95
print("%s's score is %d" % (name, score))

# format 的运用
name = 'Lily'
score = 95
print("{}'s score is {}".format(name, score))

# f-string，简化版的format
name = 'Lily'
score = 95
print(f"{name}'s score is {score}")

# 输入输出结合
name = input('Name:')
age = input('Age:')
gpa = input('GPA:')
result = 'name: %s, age: %s, gpa:%s' % (name, age, gpa)
print(result)

# 作业1

print('What is your goal of this period of study?')
goal = input()
print(goal, '?', '\nThis a good, hope you can achieve your goal.')

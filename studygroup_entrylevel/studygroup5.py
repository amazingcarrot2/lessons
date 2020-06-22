# 100以内所有3的倍数的和
result = 0
for num in range(1,100):
    if num%3 == 0:
        result = result + num
print(result)

# 2
height = input('input height:')
width = input('input width:')
for i in range(0,int(height)):
    for j in range(0,int(width)):
        print('*', end = ' ')
    print()

# 九九乘法口诀表
for i in range(1, 10):
    for j in range(1,10):
        print('%d x %d = %d' % (i, j, i*j))

# 跳出循环,当总和超过 100 时则不再继续累加
nums = [23, 45, 8, 13, 50, 43, 21]
sum = 0
for n in nums:
    if sum > 100:
        break
    sum = sum + n
print(sum)

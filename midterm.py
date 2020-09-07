# 原始数据读取
rawdata = []
with open('report.txt') as report:
    for line in report:
        line = line.strip()
        rawdata.append(line)

# 制作表头
title = '名次 ' + rawdata[0] + ' 总分' + ' 平均分'

# 原始数据去除表头以便后续操作
rawdata.pop(0)

# 计算各个学生的平均分和总分，用list储存一个学生的信息和成绩；
gradelist = []
for student in rawdata:
    new_student = []  # 新建一个列表，储存学生成绩
    student = student.split()
    new_student.append(student[0])
    total = 0
    count = 0
    for i in range(1, 10):
        score = int(student[i])  # 将成绩从str变成int再储存
        new_student.append(score)
        total += score
        count += 1
    average = round(total / count, 1)  # 计算平均分，保留一位小数
    new_student.append(total)
    new_student.append(average)
    gradelist.append(new_student)

# 计算总平均分
student_count = len(gradelist)
averagescore = ['平均']
for j in range(1, 11):
    alltotal = 0
    for new_student in gradelist:
        alltotal += new_student[j]
    averagetotal = alltotal // student_count
    averagescore.append(averagetotal)
total_average = round(averagescore[-1] / 9, 1)  # 计算总分平均分，保留一位小数
averagescore.append(total_average)

# 替换不及格的分数
for student in gradelist:
    for grade in range(1, 10):
        if student[grade] < 60:
            student[grade] = '不及格'


# 对学生的成绩进行降序排名
def taketotal(ele):
    return int(ele[-2])


gradelist.sort(key=taketotal, reverse=True)

# 制作写入文档的总表
gradelist.insert(0, averagescore)
rank = 0
for line in gradelist:
    line.insert(0, rank)
    line = ' '.join([str(x) for x in line]) + '\n'
    gradelist[rank] = line
    rank += 1
    print(line)
gradelist.insert(0, title + '\n')

with open('result.txt', 'w') as result:
    result.writelines(gradelist)

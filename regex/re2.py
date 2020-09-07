# import re
#
# m = re.match(r'\d{11}', '13913812345')
# if m:
#     print(m.group())
#
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))  # 匹配到的整体，等同于 group()
# print(m.group(1))  # 第一个括号中的分组 010
# print(m.group(2))  # 第二个括号中的分组 12345
#
# r = re.search(r'10+', '1000000') #贪婪匹配，尽可能多的0
# print(r.group())
#
# r = re.search(r'10+?', '1000000') #非贪婪匹配，一旦匹配成功就停止
# print(r.group())

import re
rule = re.compile(r'\d{3}-\d{3,8}')
tests = ['010-12345', '025-45678', '+86-1319999', '021-8888', '020-1234567']
for t in tests:
    m = rule.match(t)
    if m:
        print(m.group())
    else:
        print('不匹配')

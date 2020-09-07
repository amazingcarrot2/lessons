import re

text = "Hi, I am Shirley Hilton 123. I am his wife. 456"

# 取出 text 中所有连续的数字
regex = re.compile(r'\d+')
m = re.findall(regex, text)
print(m)

# 取出 text 中所有的单词（不包括数字）
regex = re.compile(r'\b[A-z]*[A-z]\b')
n = re.findall(regex, text)
print(n)

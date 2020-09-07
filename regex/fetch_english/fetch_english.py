import re

with open('from.txt') as fin:
    lines = fin.readlines()
    lines = ''.join(lines)

regex = re.compile(r'\b[A-z]+\b')
m = regex.findall(lines)

with open('to.txt', 'w') as f:
    for i in m:
        f.writelines(i + '\n')

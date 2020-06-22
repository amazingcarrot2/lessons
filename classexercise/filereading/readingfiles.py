txt = ['hello\n', 'how are you?\n', 'I am fine, thank you\n']
with open('data.txt', 'w') as f:
    f.writelines(txt)

with open('data.txt') as fin:
    lines = fin.readlines()
    print(lines)
    i = 0
    for line in lines:
        print(line)
        i += 1
        with open('fout%d.txt' % i, 'w') as fout:
            fout.writelines(line)

import os


def filefind(keyword, path):
    files = os.listdir(path)
    result = []
    for file in files:
        #先找文件名中含有关键字的文件
        if keyword in file:
            result.append(file)
        else:
            with open(file) as f:
                while f.readline():
                    line = f.readline()
                    #文件内容包含关键字的
                    if keyword in line:
                        result.append(file)
                        break
    print(result)


keyword = input('please input your keyword:')
path = input('please in input your path:')
filefind(keyword, path)

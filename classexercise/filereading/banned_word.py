# encoding=utf-8
import jieba


# 读取屏蔽词文件
def get_banned(bannedfile):
    bannedlist = []
    # 可以选取指定文件作为屏蔽词
    with open('%s.txt' % bannedfile, 'r') as word:
        banned_word = word.readlines()
        # print(banned_word)
    # 将屏蔽词加入到新的list中输出，并加入jieba分词词库
    for word in banned_word:
        word = word.strip()
        bannedlist.append(word)
        jieba.add_word(word)
    # print(bannedlist)
    return bannedlist


# 将输入的句子用jieba进行分词
def splitword(rawdata, bannedfile):
    bannedlist = get_banned(bannedfile)
    raw_list = jieba.lcut(rawdata)
    print(raw_list)
    ch = '*'
    for word in raw_list:
        if word in bannedlist:
            i = raw_list.index(word)
            raw_list[i] = ch * len(word)
    result = ''.join(raw_list)
    print(result)


rawdata = input('input your sentence:')
splitword(rawdata, 'banned_word')

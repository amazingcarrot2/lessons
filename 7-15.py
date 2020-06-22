list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit',
          'is', 'better', 'than', 'implicit']


def count_ele(l):
    list_1 = set(l)
    dic = dict()
    for k in list_1:
        dic[k] = l.count(k)
    print(dic)
    return dic


if __name__ == '__main__':
    list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit',
              'is', 'better', 'than', 'implicit']
    count_ele(list_s)

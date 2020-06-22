"""
【问题描述】
三人斗地主手牌规则：

一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。

要求：

将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。

可使用 list 和 random 完成。
"""
import random

list1 = ['Spade', 'Club', 'Diamond', 'Heart']
list2 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
pokers = ['Color joker', 'Black joker']
for i in list1:
    for j in list2:
        pokers.append(i + j)
random.shuffle(pokers)
l = pokers[-3:]
pokers = pokers[:-3]
player1 = pokers[0::3]
player2 = pokers[1::3]
player3 = pokers[2::3]
print(player1,
      player2,
      player3,
      l)

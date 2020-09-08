# 【问题描述】
# 奥运会期间，奖牌榜备受关注。奖牌榜上的信息每天都在更新。
#
# 要求：运用面向对象的知识，构造一个类来描述每个国家的奖牌情况。
# 类的属性包括：国家名、金/银/铜牌数量
# 再提供方法：新增奖牌、输出奖牌榜信息、获取奖牌总数等
#
# 然后创建几个国家的奖牌数据，分别按金牌数和奖牌总数对奖牌榜列表进行排序


class Country:
    def __init__(self, name, gold, silver, bronze):
        self.country = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def gain_metal(self, rank):
        if rank == 1:
            self.gold += 1
        if rank == 2:
            self.silver += 1
        elif rank == 3:
            self.bronze += 1
        else:
            pass

    def total_metal(self):
        return sum(self.gold + self.silver + self.bronze)

    def __str__(self):
        return '%s: 金牌 %d, 银牌 %d, 铜牌 %d, 总奖牌数 %d' % (
            self.country, self.gold, self.silver, self.bronze,
            self.total_metal()
        )

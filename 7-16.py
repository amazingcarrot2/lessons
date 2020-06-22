"""
【问题描述】
很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。

现在，请你帮他们设计并生成200个优惠券号码：

优惠码的字符由26个英文字符（大小写）组成
每个优惠码有8位
"""

import random
import string

letters = list(string.ascii_letters)
random.shuffle(letters)
result = []
while len(result) < 201:
    random.shuffle(letters)
    letter = ''.join(letters[:8])
    if letter not in result:
        result.append(letter)
    else:
        continue
print(result)


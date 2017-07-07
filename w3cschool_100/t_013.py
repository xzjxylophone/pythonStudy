#!/usr/bin/python
# coding=utf-8

# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。




def getNumber(start, end):
    lists = []
    if (start > end or end > 999):
        print "data error"
        return lists

    for i in range(start, end + 1, 1):
        hundred = int(i / 100)
        hundredRemain = i % 100
        ten = int(hundredRemain / 10)
        tenRemain = i % 10
        value = hundred ** 3 + ten ** 3 + tenRemain ** 3
        if (i == value):
            lists.append(i)

    return lists


lists = getNumber(100, 999)
for tmp in lists:
    print tmp





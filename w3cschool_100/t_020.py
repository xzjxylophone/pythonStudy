#!/usr/bin/python
# coding=utf-8


# 题目: 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


def printHeightAndDistance(count):
    startHeight = 100.0;
    height = startHeight;
    total = startHeight;
    for i in range(0, count):
        height = (height / 2.0)
        # 最后一次落地的时候不用再添加添加相关的距离
        if (i != count - 1):
            total += (height * 2)

    print "total: %f, height: %f" %(total, height)


printHeightAndDistance(10)








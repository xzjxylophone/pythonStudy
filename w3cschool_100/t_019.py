#!/usr/bin/python
# coding=utf-8


# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def printCompleteNumber(maxNumber):
    if (maxNumber <= 2):
        return

    for i in range(2, maxNumber + 1):
        # 因子集合, 肯定是有1这个因子
        yinziList = ["1"]
        # 寻找这个数的所有因子, 不包括自己
        # 结束条件是这个数的一半(包括此一半)
        total = i - 1;
        maxJ = int(i / 2) + 1;
        for j in range(2, maxJ):
            if (i % j == 0):
                yinziList.append(str(j))
                total -= j

        if (total == 0):
            print "complete number:", i
            print " ".join(yinziList)


printCompleteNumber(1000);


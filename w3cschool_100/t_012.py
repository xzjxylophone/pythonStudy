#!/usr/bin/python
# coding=utf-8

# 题目：判断101-200之间有多少个素数，并输出所有素数。

import math

total = 0

def printPrimeNumber(start, end):
    if (start > end):
        print "data error"
        return

    if (start <= 1):
        print "data error"
        return

    global total
    realStart = start;
    if (start % 2 == 0):
        realStart = start + 1
    realEnd = end + 1
    step = 2
    for i in range(realStart, realEnd, step):
        maxDivide = int(math.sqrt(i))
        find = 0
        for j in range(2, maxDivide + 1):
            if ((i % j) == 0):
                find = 1
                break
        if (find == 0):
            total += 1
            print i

    print "total:", total


printPrimeNumber(101, 200)





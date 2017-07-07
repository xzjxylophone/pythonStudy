#!/usr/bin/python
#coding=utf-8

# 输入三个整数x,y,z，请把这三个数由小到大输出。

def fromSmallToBig(x, y, z):
    results = []
    if (x < y):
        if (x < z):
            results.append(x)
            if (y < z):
                results.append(y)
                results.append(z)
            else:
                results.append(z)
                results.append(y)
        else:
            results.append(z)
            results.append(x)
            results.append(y)
    else:
        if (y > z):
            results.append(z)
            results.append(y)
            results.append(x)
        else:
            results.append(y)
            if (z > x):
                results.append(x)
                results.append(z)
            else:
                results.append(z)
                results.append(x)
    for val in results:
        print val



def fromSmallToBig2(x, y, z):
    lists = [x, y, z]
    lists.sort()
    for val in lists:
        print val


fromSmallToBig(8, 5, 6)
fromSmallToBig2(8, 5, 6)



#!/usr/bin/python
# coding=utf-8

# 题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？


import math
result = 0
for i in range(1, 10001):
    i1 = i + 100
    i2 = i + 268
    x = int(math.sqrt(i1))
    y = int(math.sqrt(i2))
    if (x * x == i1) and (y * y == i2):
        print i













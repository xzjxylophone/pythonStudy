#!/usr/bin/python
# coding=utf-8


# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import math

# from sys import stdout
# n = int(raw_input("input number:\n"))
# print "n = %d" % n
# for i in range(2,n + 1):
#     while n != i:
#         if n % i == 0:
#             stdout.write(str(i))
#             stdout.write("*")
#             n = n / i
#         else:
#             break
# print "%d" % n

def fenJie(number):
    if (number <= 0):
        print "data error"
        return

    if (number == 1):
        print "1 = 1 * 1"
        return

    isPrimeNumber = 1
    maxDivide = int(math.sqrt(number))
    for i in range(2, maxDivide):
        if ((number % i) == 0):
            isPrimeNumber = 0
            break

    if (isPrimeNumber == 1):
        print "%d = 1 * %d" %(number, number)
        return

    lists = []
    tmpNumber = number
    for i in range(2, tmpNumber + 1):
        while (tmpNumber != i + 1):
            if (tmpNumber % i == 0):
                lists.append(str(i))
                tmpNumber = tmpNumber / i
            else:
                break

    code = " * ".join(lists)
    print "lists: ", lists
    print "%d = %s" %(number, code)



fenJie(100)


#!/usr/bin/python
#coding=utf-8


# 题目：斐波那契数列。


def fibonacci(number):
    if (number <= 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)



def fibonacci2(number):
    a = 1
    b = 1
    for i in range(number - 1):
        # a,b = b, a+b
        # 等价于
        tmp = a
        a = b
        b = tmp + b
    return a

result = fibonacci(10)
print "result: ", result



result = fibonacci2(10)
print "result: ", result



